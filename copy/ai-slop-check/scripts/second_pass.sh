#!/usr/bin/env bash
# Second editing pass by a different model family than the one that drafted.
#
#   scripts/second_pass.sh draft.md > edited.md 2> notes.txt          # Claude drafted, Codex edits
#   WRITER=gpt scripts/second_pass.sh draft.md > edited.md            # GPT drafted, Claude edits
#
# Edited copy goes to stdout, change notes to stderr. If the rival CLI is not
# installed, the prompt plus draft is printed to stdout and the script exits 127,
# so paste that into ChatGPT (or Claude) by hand. Exit 124 means it timed out.
# Always rerun scripts/check_tells.py on the result.
#
# The rival-model idea comes from SlopMonster (github.com/ItsssssJack/SlopMonster, MIT).
set -uo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
PROMPT="$HERE/../references/second-pass-prompt.md"
TIMEOUT="${TIMEOUT:-240}"
WRITER="${WRITER:-claude}"

if [ $# -eq 0 ] || [ "$1" = "-" ]; then DRAFT="$(cat)"; else
  [ -r "$1" ] || { echo "second_pass: cannot read $1" >&2; exit 66; }
  DRAFT="$(cat "$1")"
fi
[ -n "$(printf '%s' "$DRAFT" | tr -d '[:space:]')" ] || { echo "second_pass: draft is empty" >&2; exit 66; }
FULL="$(cat "$PROMPT")
$DRAFT"

find_bin() {
  for c in "$(command -v "$1" 2>/dev/null)" "$HOME/.local/bin/$1" "/opt/homebrew/bin/$1" \
           "/Applications/Codex.app/Contents/Resources/$1"; do
    [ -n "$c" ] && [ -x "$c" ] && { echo "$c"; return 0; }
  done
  return 1
}

run_bounded() {   # macOS has no `timeout`
  local out; out="$(mktemp)"
  "$@" >"$out" 2>/dev/null </dev/null & local pid=$! waited=0
  while kill -0 "$pid" 2>/dev/null; do
    if [ "$waited" -ge "$TIMEOUT" ]; then
      kill -9 "$pid" 2>/dev/null; rm -f "$out"
      echo "second_pass: timed out after ${TIMEOUT}s" >&2; return 124
    fi
    sleep 2; waited=$((waited + 2))
  done
  wait "$pid"; local rc=$?; cat "$out"; rm -f "$out"; return $rc
}

split() {   # copy to stdout, notes to stderr
  awk '$0=="<<<NOTES>>>"{n=1;next} n{print > "/dev/stderr";next} {print}
       END{if(!n) print "second_pass: WARNING no <<<NOTES>>> line; check the end of the copy for stray notes" > "/dev/stderr"}'
}

if [ "$WRITER" = "gpt" ]; then RIVAL="claude"; else RIVAL="codex"; fi
BIN="$(find_bin "$RIVAL" || true)"

if [ -z "$BIN" ]; then
  echo "second_pass: no $RIVAL CLI found. Paste everything below into $([ "$RIVAL" = codex ] && echo ChatGPT || echo Claude):" >&2
  printf '%s\n' "$FULL"
  exit 127
fi

if [ "$RIVAL" = "codex" ]; then
  RAW="$(run_bounded "$BIN" exec --skip-git-repo-check --sandbox read-only "$FULL")" || exit $?
  # codex exec prints banners; the answer sits after the last bare "codex" line.
  BODY="$(printf '%s\n' "$RAW" | awk '$0=="codex"{b="";on=1;next} $0=="tokens used"{on=0;next} on{b=b $0 "\n"} END{printf "%s", b}')"
  [ -n "$(printf '%s' "$BODY" | tr -d '[:space:]')" ] || BODY="$RAW"
  printf '%s\n' "$BODY" | split
else
  RAW="$(run_bounded "$BIN" -p "$FULL")" || exit $?
  printf '%s\n' "$RAW" | split
fi
