# How predictable is English? Bits per letter, given the last n letters.
from math import log2
from markov import train
from text import load, ALPHABET

text = load()
cut = int(len(text) * 0.9)
train_text, test_text = text[:cut], text[cut:]

def cross_entropy(n, alpha=0.1):
    model = train(train_text, n)
    bits = 0.0
    for i in range(n, len(test_text)):
        seen = model[test_text[i - n:i]]
        count = seen[test_text[i]] + alpha          # add a little to
        total = sum(seen.values()) + alpha * 27     # every letter
        bits += -log2(count / total)
    return bits / (len(test_text) - n)

if __name__ == '__main__':
    for n in range(0, 7):
        h = cross_entropy(n)
        print(f'last {n} letters: {h:.2f} bits  perplexity {2**h:.1f}')
