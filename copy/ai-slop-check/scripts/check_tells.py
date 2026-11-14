#!/usr/bin/env python3
"""Flag AI copy tells in a draft. Standard library only, no network.

    python3 check_tells.py draft.md
    python3 check_tells.py page.html
    python3 check_tells.py --text "Paste the draft here."
    cat draft.txt | python3 check_tells.py -
    python3 check_tells.py draft.md --skip hedge,emoji      # turn rules off
    python3 check_tells.py --list-rules

Exit status is 0 when nothing is flagged and 1 when anything is. A hit is a
prompt to reread the sentence, not a verdict: review each one in context.

The idea of a deterministic pass before (and after) the model edit comes from
SlopMonster (github.com/ItsssssJack/SlopMonster, MIT). The rules here are
written from the ai-slop-check (formerly ai-copy-tells) pattern list, not ported from that repo.
"""
import html as _html
import re
import sys

# ── rule registry ────────────────────────────────────────────────────────────
RULES = {
    'echo':        'parallel repetition: consecutive sentences open with the same word',
    'contrast':    'false contrast ("not just X", "isn\'t X, it\'s Y", "It\'s not X. It\'s not Y.")',
    'staccato':    'three short sentences in a row',
    'rhetorical':  'rhetorical question answered by the next line',
    'imagine':     '"imagine" opener',
    'filler':      'filler transition',
    'hedge':       'hedging word (keep only where compliance requires it)',
    'rejected':    'phrasing from the rejected-lines list',
    'vocab':       'AI buzzword',
    'colon':       'colon that does not introduce a list',
    'em-dash':     'em dash or dash used as one',
    'arrow':       'arrow glyph (not allowed in CTAs or links)',
    'emoji':       'emoji',
    'exclaim':     'more than one exclamation point in the draft',
    'dense':       'paragraph of five or more sentences',
    'proof':       'number next to clients/leads/customers: verify, and never publish raw client counts',
    'here-opener': 'sentence opens with "Here\'s" / "Here is" / "Here are" to announce what comes next',
    'real-closer': '"That\'s the real X" line crowning the point',
    'reveal':      'stock reveal or honesty interjection ("what nobody tells you", "honestly", "then I realized")',
    'assistant':   'leaked chatbot phrasing ("as an AI language model", "I hope this helps")',
    'title-template': '"From X to Y" title or "Master X in N days" template',
}

FILLER = [
    r"let'?s dive in", r"here'?s the thing", r"at the end of the day",
    r"in today'?s (?:fast-paced|digital|ever-changing|modern|dynamic|evolving)", r"whether you'?re an? .{1,40}? or an?\b",
    r"as the world (?:continues to )?(?:evolve|evolves|change|changes)", r"no fluff",
    r"shout(?:ing|s)? into the void",
    r"more on that later", r"but wait,? there'?s more", r"without further ado",
    r"say goodbye to", r"(?:that|this)(?:'s| is) where .{1,30}? comes? in", r"look no further",
    r"buckle up", r"the best part\??", r"the secret sauce", r"in a world where",
]

HEDGE = [
    r"might", r"could potentially", r"may potentially", r"in many cases",
    r"often", r"usually", r"can help you", r"helps? you to", r"arguably",
    r"tends? to",
]

# Lines a reader rejected as "I would never say this", generalised to the pattern.
REJECTED = [
    (r"in the way the word suggests",            'pedantic qualifier'),
    (r"\bonly takes?\b|\bthat'?s all it takes\b|\bthe whole job\b|\bthat'?s it\b", '"it\'s easy" reassurance'),
    (r"has nothing to do with|\bnot because you'?re\b|\band it'?s not your fault\b", 'denial nobody raised'),
    (r"\bi want to show you\b|\blet me show you\b|hiding in plain sight|\bthe posts? below\b", 'announcing what\'s coming'),
    (r"\b(?:it'?s|is|are) (?:really |actually )?(?:simple|easy|straightforward)\b|\bthe upgrade path\b", '"it\'s simple" framing'),
    (r"\bconnect the two\b|\bthe (?:lightweight|heavier|lighter|simple|advanced) version\b", 'vague referent or invented label'),
    (r"\bthe boring way\b|\bwhich is exactly why\b", 'folksy justification'),
    (r"\bi learned why\b|\bi learned (?:the hard way|that) .{0,40}matters\b", 'lesson-learned setup'),
    (r"you'?re the only one who knows|\bin (?:ten|10|five|5) seconds\b|\bupgrade what comes back\b", 'coaching voice or fake precision'),
    (r"\bbelow\b.{0,30}\btakes? about\b", 'reference the reader can\'t follow yet'),
]

VOCAB = [
    r"delv(?:e|es|ed|ing)", r"seamless(?:ly)?", r"unlock(?:s|ed|ing)?", r"unleash(?:es|ed|ing)?",
    r"elevat(?:e|es|ed|ing)", r"leverag(?:e|es|ed|ing)", r"robust", r"empower(?:s|ed|ing)?",
    r"streamlin(?:e|es|ed|ing)", r"game-?chang(?:er|ing)", r"revolutioni[sz](?:e|es|ed|ing)",
    r"transformative", r"transformation(?:al)?", r"tapestry", r"testament to", r"beacon", r"unparalleled",
    r"supercharg(?:e|es|ed|ing)", r"turbocharg(?:e|es|ed|ing)", r"effortless(?:ly)?",
    r"next-level", r"cutting-edge", r"state-of-the-art", r"world-class", r"best-in-class",
    r"holistic", r"synerg(?:y|ies)", r"paradigm", r"bespoke", r"meticulous(?:ly)?",
    r"pivotal", r"foster(?:s|ed|ing)?", r"harness(?:es|ed|ing)? the power",
    r"navigat(?:e|es|ed|ing) (?:the|your|this|these|today'?s|an?)", r"ever-evolving", r"realm", r"landscape",
    r"embark(?:s|ed|ing)?",
    r"journey", r"curated", r"myriad", r"plethora", r"deep dive", r"level up",
    r"it'?s (?:important|worth) (?:to note|noting)", r"underscores?",
    r"quietly", r"grounded",
]

# Stock reveal and honesty interjections. Bans the phrasing, not a hook that
# withholds a specific answer ("the SEO tool you're not using, but should be").
REVEAL = [
    r"what (?:nobody|no one) (?:tells you|talks about|is talking about|will tell you)",
    r"the secret (?:nobody|no one)", r"(?:nobody|no one) (?:is )?talking about",
    r"honestly", r"to be honest", r"truth is", r"then i realized",
    r"that'?s when it (?:hit|clicked for) me", r"it hit me",
]

ASSISTANT = [
    r"as an ai (?:language )?model", r"as an ai assistant", r"as a (?:large )?language model",
    r"i hope this helps", r"great question", r"i'?m (?:just )?an ai(?: model)?",
]

MASTER_TEMPLATE = re.compile(
    r"\bmaster(?:ing)? .{1,40}? in (?:\d+|one|two|three|five|seven|ten|thirty) "
    r"(?:days?|weeks?|hours?|minutes?|steps?)\b", re.I)
# "From X to Y" in a title. A money or number range ("from $500 to $900") is fine.
FROM_TO_TEMPLATE = re.compile(r"\bfrom (?![$\d])[\w'-]+(?: [\w'-]+){0,4} to\b", re.I)

CONTRAST = [
    r"\bnot just\b", r"\bmore than just\b", r"\bnot only\b.{0,60}\bbut\b",
    r"\b(?:is|was|are)n'?t (?:just |only |about )?(?:a |an |the )?[^.,;!?]{1,40}[,;.]\s+(?:it|this|that|they)(?:'s| is| are|'re)\b",
    r"\bisn'?t about\b.{0,60}\bit'?s about\b",
]

ARROW = re.compile(r"[←-⇿➡➔-➿⬅-⬇➜]|->|=>")
EMOJI = re.compile(r"[\U0001F000-\U0001FAFF☀-⛿✀-➓]")
EM_DASH = re.compile(r"\u2014|\s--\s|\s\u2013\s")
PROOF = re.compile(
    r"\b\d[\d,]*(?:\.\d+)?\+?\s+(?:\w+\s+)?"
    r"(?:clients?|customers?|leads?|calls?|patients?|users?|businesses|students?"
    r"|subscribers?|bookings?|sales|deals|reviews|visitors?|members?)\b", re.I)
LIST_ITEM = re.compile(r"^\s*(?:[-*+•]|\d+[.)])\s+")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+")
SENT_SPLIT = re.compile(r"(?<=[.!?])[\"'”’)]*\s+(?=[\"'“‘(]?[A-Z0-9])")


def compile_list(pats, flags=re.I):
    return [re.compile(rf"(?<![\w-])(?:{p})(?![\w-])", flags) for p in pats]


FILLER_RE, HEDGE_RE, VOCAB_RE, CONTRAST_RE = (
    compile_list(FILLER), compile_list(HEDGE), compile_list(VOCAB),
    [re.compile(p, re.I) for p in CONTRAST])
REVEAL_RE, ASSISTANT_RE = compile_list(REVEAL), compile_list(ASSISTANT)
REJECTED_RE = [(re.compile(p, re.I), label) for p, label in REJECTED]


# ── input cleanup ────────────────────────────────────────────────────────────
def normalise(t):
    return (t.replace('’', "'").replace('‘', "'").replace(' ', ' ')
             .replace('‑', '-'))


def html_to_lines(src):
    t = re.sub(r'<(script|style|noscript)\b.*?</\1>', ' ', src, flags=re.S | re.I)
    t = re.sub(r'<!--.*?-->', ' ', t, flags=re.S)
    t = re.sub(r'<li\b[^>]*>', '\n- ', t, flags=re.I)
    t = re.sub(r'<h[1-6]\b[^>]*>', '\n# ', t, flags=re.I)
    t = re.sub(r'</?(?:p|div|br|h[1-6]|section|article|header|footer|ul|ol|tr|td|th|blockquote|a|button)\b[^>]*>',
               '\n', t, flags=re.I)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = _html.unescape(t)
    return [re.sub(r'[ \t]+', ' ', ln).strip() for ln in t.split('\n')]


def markdown_lines(src):
    """Keep line numbers stable: blank out what is not prose instead of deleting it."""
    lines = src.split('\n')
    out, in_fence, in_front = [], False, False
    for i, ln in enumerate(lines):
        if i == 0 and ln.strip() == '---':
            in_front = True
            out.append('')
            continue
        if in_front:
            if ln.strip() == '---':
                in_front = False
            out.append('')
            continue
        if ln.lstrip().startswith('```'):
            in_fence = not in_fence
            out.append('')
            continue
        if in_fence:
            out.append('')
            continue
        ln = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', ln)          # images
        ln = re.sub(r'!\[\[[^\]]*\]\]', ' ', ln)                 # Obsidian embeds
        ln = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', ln)       # links keep their text
        ln = re.sub(r'\[\[([^\]|]*\|)?([^\]]*)\]\]', r'\2', ln)  # wikilinks
        ln = re.sub(r'`[^`]*`', 'X', ln)                      # inline code
        ln = re.sub(r'~~.*?~~', 'X', ln)                      # struck-out specimens
        ln = re.sub(r'<[^>]+>', ' ', ln)
        ln = re.sub(r'^\s*(?:>\s?)+', '', ln)                  # blockquotes
        ln = re.sub(r'\[![\w-]+\][+-]?', '', ln)               # Obsidian callout markers
        out.append(ln)
    return out


def mask_for_colon(s):
    s = re.sub(r'https?://\S+|www\.\S+', 'URL', s)
    s = re.sub(r'\b\d{1,2}:\d{2}\b', 'TIME', s)
    s = re.sub(r'\b\d+:\d+\b', 'RATIO', s)
    return s


# ── checks ───────────────────────────────────────────────────────────────────
def words(s):
    return re.findall(r"[A-Za-z0-9']+", s)


# Opening words too common to count as an echo on their own. A pair still
# flags when the first two words match or both sentences are short.
COMMON_OPENERS = {'the', 'a', 'an', 'if', 'and', 'but', 'so', 'on', 'in', 'for', 'to',
                  'with', 'when', 'as', 'at', 'of', 'i', 'you', 'we', 'my', 'your'}


def first_word(s):
    w = words(s)
    return w[0].lower() if w else ''


def audit(lines, skip):
    hits = []

    def add(rule, line_no, text, note=''):
        if rule not in skip:
            hits.append((line_no, rule, text.strip(), note))

    # Units: every prose sentence with its line number, in reading order.
    sentences = []   # (line_no, sentence, is_heading, is_list)
    for idx, raw in enumerate(lines, 1):
        ln = normalise(raw).strip()
        if not ln:
            continue
        is_heading = bool(HEADING.match(ln))
        is_list = bool(LIST_ITEM.match(ln))
        body = HEADING.sub('', LIST_ITEM.sub('', ln)).strip()
        if not body:
            continue

        # Character-level rules run on the whole line.
        if EM_DASH.search(body):
            add('em-dash', idx, body)
        if ARROW.search(body):
            add('arrow', idx, body)
        if EMOJI.search(body):
            add('emoji', idx, body)

        masked = mask_for_colon(body)
        if ':' in masked:
            after = masked.split(':', 1)[1].strip()
            if after:
                add('colon', idx, body, 'setup: payoff colon' + (' in a heading' if is_heading else ''))
            else:
                nxt = next((normalise(l) for l in lines[idx:] if l.strip()), '')
                if not LIST_ITEM.match(nxt):
                    add('colon', idx, body, 'line ends in a colon but no list follows')

        for s in SENT_SPLIT.split(body):
            if s.strip():
                sentences.append((idx, s.strip(), is_heading, is_list))

    # Phrase and word rules, per sentence.
    for line_no, s, is_heading, _ in sentences:
        low = s.lower()
        for rx in FILLER_RE:
            if rx.search(low):
                add('filler', line_no, s, rx.search(low).group(0))
        for rx in HEDGE_RE:
            m = rx.search(low)
            if m:
                add('hedge', line_no, s, m.group(0))
        for rx, label in REJECTED_RE:
            if rx.search(low):
                add('rejected', line_no, s, label)
        found = sorted({rx.search(low).group(0) for rx in VOCAB_RE if rx.search(low)})
        if found:
            add('vocab', line_no, s, ', '.join(found))
        for rx in CONTRAST_RE:
            if rx.search(low):
                add('contrast', line_no, s)
                break
        if re.match(r"\s*imagine\b", low):
            add('imagine', line_no, s)
        if re.match(r"\s*here(?:'s| is| are)\b", low) and not re.match(r"\s*here'?s the thing\b", low):
            add('here-opener', line_no, s)
        if re.search(r"\b(?:that|this)(?:'s| is) the real\b", low):
            add('real-closer', line_no, s)
        for rx in REVEAL_RE:
            m = rx.search(low)
            if m:
                add('reveal', line_no, s, m.group(0))
                break
        m = next((rx.search(low) for rx in ASSISTANT_RE if rx.search(low)), None)
        if m or re.match(r"\s*certainly[!,.]", low):
            add('assistant', line_no, s, m.group(0) if m else 'certainly')
        if MASTER_TEMPLATE.search(s):
            add('title-template', line_no, s, '"Master X in N days"')
        elif FROM_TO_TEMPLATE.search(s) and (
                is_heading or (low.startswith('from ') and len(words(s)) <= 10)):
            add('title-template', line_no, s, '"From X to Y"')
        for m in PROOF.finditer(s):
            add('proof', line_no, s, m.group(0))

    # Sequence rules. A heading starts a new run.
    not_rx = r"(?:it'?s|this is|that'?s|it is) not\b|(?:it|this|that) isn'?t\b"
    run, short = [], []

    def flush_short():
        if len(short) >= 3:
            add('staccato', short[0][0], ' / '.join(x[1] for x in short), f'{len(short)} in a row')
        short.clear()

    for item in sentences:
        if item[2]:
            run = []
            flush_short()
            continue
        run.append(item)
        if len(run) >= 2:
            (l1, s1, _, _), (l2, s2, _, _) = run[-2], run[-1]
            w1, w2 = first_word(s1), first_word(s2)
            if re.match(not_rx, s1.lower()) and re.match(not_rx, s2.lower()):
                add('contrast', l2, f'{s1} / {s2}', 'stacked "It\'s not" sentences')
            elif w1 and w1 == w2 and not (run[-2][3] and run[-1][3]) and (
                    w1 not in COMMON_OPENERS
                    or words(s1)[:2] == words(s2)[:2]
                    or max(len(words(s1)), len(words(s2))) <= 8):
                add('echo', l2, f'{s1} / {s2}', f'both open with "{w1}"')
            if s1.endswith('?') and len(words(s1)) <= 9 and not s2.endswith('?'):
                add('rhetorical', l1, f'{s1} / {s2}',
                    'one-word question answered on the spot' if len(words(s1)) <= 3 else '')
        # Short sentences in a row; list items and list intros don't count.
        _, s, _, is_list = item
        if not is_list and not s.endswith(':') and len(words(s)) <= 6:
            short.append(item)
        else:
            flush_short()
    flush_short()

    # Draft-level rules.
    bangs = [(i, l) for i, l in enumerate(lines, 1) if '!' in l]
    if sum(l.count('!') for _, l in bangs) > 1:
        for i, l in bangs:
            add('exclaim', i, normalise(l))

    para, start = [], None
    for idx, raw in enumerate(lines + [''], 1):
        ln = raw.strip()
        if ln and not HEADING.match(ln) and not LIST_ITEM.match(ln):
            start = start or idx
            para.append(ln)
            continue
        if para:
            n = len([s for s in SENT_SPLIT.split(' '.join(para)) if s.strip()])
            if n >= 5:
                add('dense', start, ' '.join(para)[:120] + ('...' if len(' '.join(para)) > 120 else ''),
                    f'{n} sentences')
        para, start = [], None

    # De-duplicate (same line, rule, note) and sort by line.
    seen, out = set(), []
    for h in sorted(hits, key=lambda h: (h[0], h[1])):
        key = (h[0], h[1], h[3], h[2][:60])
        if key not in seen:
            seen.add(key)
            out.append(h)
    return out


# ── CLI ──────────────────────────────────────────────────────────────────────
def main(argv):
    try:
        sys.stdout.reconfigure(errors='replace')
    except (AttributeError, ValueError):
        pass
    if not argv or argv[0] in ('-h', '--help'):
        sys.exit(__doc__)
    if '--list-rules' in argv:
        for k, v in RULES.items():
            print(f'{k:11} {v}')
        return 0

    skip = set()
    if '--skip' in argv:
        i = argv.index('--skip')
        skip = {s.strip() for s in argv[i + 1].split(',') if s.strip()}
        unknown = skip - RULES.keys()
        if unknown:
            sys.exit(f'unknown rule(s): {", ".join(sorted(unknown))}. See --list-rules.')
        del argv[i:i + 2]

    if argv[0] == '--text':
        lines = markdown_lines(' '.join(argv[1:]).replace('\\n', '\n'))
        label = 'pasted text'
    elif argv[0] == '-':
        lines = markdown_lines(sys.stdin.read())
        label = 'stdin'
    else:
        path = argv[0]
        try:
            src = open(path, encoding='utf-8', errors='replace').read()
        except OSError as e:
            sys.exit(f'cannot read {path}: {e.strerror}')
        lines = html_to_lines(src) if path.lower().endswith(('.html', '.htm')) else markdown_lines(src)
        label = path

    if not any(l.strip() for l in lines):
        sys.exit('no copy to check: empty input')

    hits = audit(lines, skip)
    print(f'{label}: {len(hits)} flag(s)\n')
    for line_no, rule, text, note in hits:
        quote = text if len(text) <= 160 else text[:157] + '...'
        print(f'  L{line_no:<4} {rule:10} "{quote}"' + (f'  [{note}]' if note else ''))
    if hits:
        counts = {}
        for _, rule, _, _ in hits:
            counts[rule] = counts.get(rule, 0) + 1
        print('\n  by rule: ' + ', '.join(f'{k} {v}' for k, v in sorted(counts.items(), key=lambda kv: -kv[1])))
    else:
        print('  clean: no rule matched. Still read it once in context.')
    return 1 if hits else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
