#!/usr/bin/env bash
# Run Desklib's open-source AI-text detector on a draft.
#
#   scripts/detect_ai.sh draft.md            # .md, .html or .txt
#   scripts/detect_ai.sh --text "paragraph"
#
# First run builds a Python 3.12 venv with uv in ~/.local/share/ai-slop-check/desklib-venv
# and downloads the model (~1.7 GB) to the Hugging Face cache. Later runs are offline.
# Override the venv location with DESKLIB_VENV=/path.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
VENV="${DESKLIB_VENV:-$HOME/.local/share/ai-slop-check/desklib-venv}"

if [ ! -x "$VENV/bin/python" ] || ! "$VENV/bin/python" -c "import torch, transformers, sentencepiece" 2>/dev/null; then
  command -v uv >/dev/null || { echo "detect_ai: needs uv (brew install uv)" >&2; exit 69; }
  echo "detect_ai: building venv at $VENV (one time)..." >&2
  uv venv -q -p 3.12 "$VENV" >&2
  uv pip install -q -p "$VENV/bin/python" "torch>=2.4" "transformers>=4.45" sentencepiece protobuf tiktoken >&2
fi

# Quiet the HF/transformers chatter; use the cached model when it's there.
export TRANSFORMERS_VERBOSITY=error HF_HUB_DISABLE_PROGRESS_BARS=1 TOKENIZERS_PARALLELISM=false
if ls "${HF_HOME:-$HOME/.cache/huggingface}/hub/models--desklib--ai-text-detector-v1.01" >/dev/null 2>&1; then
  export HF_HUB_OFFLINE=1
fi
exec "$VENV/bin/python" -I "$HERE/detect_ai.py" "$@"
