#!/usr/bin/env python3
"""Score a draft with Desklib's open-source AI-text detector.

Run through detect_ai.sh, which builds the venv on first use:

    scripts/detect_ai.sh draft.md            # .md, .html or .txt
    scripts/detect_ai.sh page.html --threshold 0.4
    scripts/detect_ai.sh --text "Paste a paragraph here."

Prints a whole-draft score (average over ~700-token chunks), one score per
section, and every paragraph of 40+ words that scores at or above the
threshold (default 0.5). Exit status is 1 when the whole draft or any
paragraph crosses the threshold, 0 otherwise.

The model is desklib/ai-text-detector-v1.01 (DeBERTa-v3-large, MIT), which its model card
says led the RAID benchmark when submitted. Added to this skill 2026-11-09.
It is a weak signal: it has scored drafts a human editor rejected as slop
as human-written too. A low score never clears a draft; the pattern pass still decides.
A high score on a paragraph is a reason to reread it.
"""
import argparse
import html
import re
import sys

MODEL = "desklib/ai-text-detector-v1.01"
MIN_WORDS = 40


def strip_tags(s):
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def blocks_from_html(src):
    """Return [(section_title, [paragraph, ...]), ...] from the article body."""
    for tag in ("article", "main", "body"):
        m = re.search(rf"<{tag}\b[^>]*>(.*?)</{tag}>", src, re.S | re.I)
        if m:
            src = m.group(1)
            break
    # Drop things that aren't the writer's prose.
    src = re.sub(r"<!--.*?-->", "", src, flags=re.S)
    for tag in ("script", "style", "pre", "code", "figure", "nav", "footer", "form", "button"):
        src = re.sub(rf"<{tag}\b.*?</{tag}>", "", src, flags=re.S | re.I)
    # The sources list and copy-paste prompt boxes skew the score.
    src = re.split(r'<h2[^>]*id="sources"', src, flags=re.I)[0]
    src = re.sub(r'<div class="prompt">.*?</div>|<div class="byline">.*?</div>', "", src, flags=re.S)
    src = re.sub(r"<h1\b.*?</h1>", "", src, flags=re.S | re.I)
    parts = re.split(r"<h[23][^>]*>(.*?)</h[23]>", src, flags=re.S | re.I)
    out = [("Intro", parts[0])] + [(strip_tags(parts[i]), parts[i + 1]) for i in range(1, len(parts), 2)]
    res = []
    for title, body in out:
        paras = [strip_tags(p) for p in re.findall(r"<(?:p|li|blockquote)\b[^>]*>(.*?)</(?:p|li|blockquote)>", body, re.S | re.I)]
        paras = [p for p in paras if p]
        if paras:
            res.append((title, paras))
    return res


def md_clean(s):
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)               # images
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)            # links
    s = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", r"\1", s)   # wikilinks
    s = re.sub(r"[*_`]+", "", s)
    s = re.sub(r"^\s*(?:[-*+]|\d+[.)]|>)\s+", "", s, flags=re.M)
    return re.sub(r"\s+", " ", s).strip()


def blocks_from_md(src):
    src = re.sub(r"\A---\n.*?\n---\n", "", src, flags=re.S)  # frontmatter
    src = re.sub(r"```.*?```", "", src, flags=re.S)          # code / prompt blocks
    src = re.sub(r"<!--.*?-->", "", src, flags=re.S)
    res, title, paras = [], "Intro", []
    for chunk in re.split(r"\n\s*\n", src):
        head = re.match(r"^\s{0,3}(#{1,6})\s+(.*)", chunk)
        if head:
            if paras:
                res.append((title, paras))
            if re.match(r"(?i)sources|references", head.group(2).strip()):
                return res
            title, paras = head.group(2).strip(), []
            chunk = chunk[head.end():]
        t = md_clean(chunk)
        if t:
            paras.append(t)
    if paras:
        res.append((title, paras))
    return res


def load_model():
    import logging
    import warnings
    logging.disable(logging.WARNING)  # torch import-time notes on macOS
    warnings.filterwarnings("ignore")
    import torch
    import torch.nn as nn
    from transformers import AutoConfig, AutoModel, AutoTokenizer, PreTrainedModel

    class DesklibAIDetectionModel(PreTrainedModel):
        config_class = AutoConfig

        def __init__(self, config):
            super().__init__(config)
            self.model = AutoModel.from_config(config)
            self.classifier = nn.Linear(config.hidden_size, 1)
            self.post_init()  # required on transformers 5

        def forward(self, input_ids, attention_mask=None):
            h = self.model(input_ids, attention_mask=attention_mask)[0]
            m = attention_mask.unsqueeze(-1).expand(h.size()).float()
            return self.classifier((h * m).sum(1) / m.sum(1).clamp(min=1e-9))

    tok = AutoTokenizer.from_pretrained(MODEL)
    model = DesklibAIDetectionModel.from_pretrained(MODEL).eval()

    def score(text):
        enc = tok(text, truncation=True, max_length=768, return_tensors="pt")
        with torch.no_grad():
            return torch.sigmoid(model(enc["input_ids"], enc["attention_mask"])).item()

    return tok, score


def main(argv):
    ap = argparse.ArgumentParser(description="Desklib AI-text detector, a weak second signal for ai-slop-check.")
    ap.add_argument("path", nargs="?", help=".md, .html or .txt file, or - for stdin")
    ap.add_argument("--text", help="score this text instead of a file")
    ap.add_argument("--threshold", type=float, default=0.5, help="flag at or above this (default 0.5)")
    a = ap.parse_args(argv)

    if a.text:
        src, kind = a.text, "txt"
    elif a.path in (None, "-"):
        src, kind = sys.stdin.read(), "txt"
    else:
        src = open(a.path, encoding="utf-8").read()
        kind = "html" if a.path.lower().endswith((".html", ".htm")) else "md"

    if kind == "html":
        blocks = blocks_from_html(src)
    elif kind == "md":
        blocks = blocks_from_md(src)
    else:
        blocks = [("Text", [md_clean(p) for p in re.split(r"\n\s*\n", src) if p.strip()])]
    if not any(blocks):
        print("detect_ai: no prose found", file=sys.stderr)
        return 66

    tok, score = load_model()
    flagged = False

    full = " ".join(" ".join(p) for _, p in blocks)
    ids = tok(full, add_special_tokens=False)["input_ids"]
    chunks = [tok.decode(ids[i:i + 700]) for i in range(0, len(ids), 700)]
    scores = [score(c) for c in chunks]
    whole = sum(scores) / len(scores)
    flagged |= whole >= a.threshold

    print(f"Desklib AI-text score (0 = human, 1 = AI), threshold {a.threshold}\n")
    for title, paras in blocks:
        s = score(" ".join(paras))
        mark = "  <<" if s >= a.threshold else ""
        print(f"{s:.3f}  {len(' '.join(paras).split()):4d} words  {title[:70]}{mark}")
        for p in paras:
            if len(p.split()) >= MIN_WORDS:
                ps = score(p)
                if ps >= a.threshold:
                    flagged = True
                    print(f"        {ps:.3f}  \"{p[:110]}{'...' if len(p) > 110 else ''}\"")
    print(f"\nWHOLE DRAFT: {whole:.3f} (avg of {len(chunks)} chunk{'s' if len(chunks) != 1 else ''}: "
          f"{', '.join(f'{x:.3f}' for x in scores)}; {len(full.split())} words)")
    print("Weak signal. A low score never clears a draft; reread any flagged paragraph against the patterns.")
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
