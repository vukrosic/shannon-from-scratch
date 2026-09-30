# Learn everything Claude Shannon knew — from scratch

Code for the video course. Every file is one step, in the order the video teaches it. Each is under 40 lines of plain Python (no libraries) and runs on the included Shakespeare text (`shakespeare.txt`, ~1.1 M characters).

```bash
./run_all.sh            # run every step, output as in demo-output.txt
python3 markov.py       # generate text with 0–5 letters of memory
python3 markov.py your_text.txt
```

| Step | File | Shannon's idea | Year |
| --- | --- | --- | --- |
| 1 | `switches.py` | Relay switches do Boolean logic; add binary numbers | 1937 |
| 2 | `surprise.py` | Surprise = log2(1/p) bits; entropy of a coin | 1948 |
| 3 | `text.py`, `letters.py` | Letter frequencies; entropy of English letters (4.08 bits) | 1948 |
| 4 | `markov.py` | Letter n-gram language model that writes text | 1948 |
| 5 | `words.py` | Word-level model ("my" → lord, heart, father…) | 1948 |
| 6 | `predict.py` | Cross-entropy and perplexity vs context length | 1951 |
| 7 | `huffman.py` | Huffman code (4.13 bits/letter) vs 5-bit fixed code and zlib | 1952 |
| 8 | `channel.py` | Noisy channel: repetition codes vs capacity C = 1 − H(0.1) = 0.531 | 1948 |
| 9 | `hamming.py` | Hamming (7,4) code finds and fixes a flipped bit | 1950 |
| 10 | `secret.py` | One-time pad; another key decrypts to any message | 1949 |
| 11 | `chess.py` | Minimax; tic-tac-toe with perfect play is a draw | 1950 |

`values.py` computes every number shown on screen and writes `values.json`.

## Results on this text

- Letters equally likely: 4.75 bits per letter. Real letter counts: 4.08 bits.
- Best n-gram context is 4 letters: 2.20 bits per letter (perplexity 4.6). Longer contexts get worse because most 5- and 6-letter contexts were seen too rarely.
- Huffman: 546,951 bytes (4.13 bits/letter) vs 662,237 bytes for a fixed 5-bit code. zlib: 2.85 bits/letter.
- Binary channel flipping 10 % of bits: capacity 0.531 bits per sent bit.

License: MIT.
