# How many bits does one letter of English carry?
from collections import Counter
from surprise import entropy
from math import log2
from text import load, ALPHABET

text = load()
counts = Counter(text)
total = len(text)
probs = {c: counts[c] / total for c in ALPHABET}

if __name__ == '__main__':
    print('characters   :', total)
    for c in sorted(probs, key=probs.get, reverse=True)[:6]:
        print(repr(c), round(probs[c] * 100, 1), '%')
    print('all equal    :', round(log2(27), 2), 'bits per letter')
    print('real English :', round(entropy(probs.values()), 2), 'bits')
