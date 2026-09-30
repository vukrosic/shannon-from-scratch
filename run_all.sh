#!/usr/bin/env bash
# Run every step in video order and print what each one finds.
set -e
cd "$(dirname "$0")"
for s in switches surprise letters markov words predict huffman channel hamming secret chess; do
  echo "## $s"
  python3 "$s.py"
done
