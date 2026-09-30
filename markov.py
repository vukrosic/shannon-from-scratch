# Shannon's 1948 language model: guess the next letter from the last n.
import random
import sys
from collections import Counter, defaultdict
from text import load, ALPHABET

def train(text, n):
    model = defaultdict(Counter)
    for i in range(n, len(text)):
        model[text[i - n:i]][text[i]] += 1
    return model

def generate(model, n, length, seed=0):
    rng = random.Random(seed)
    out = rng.choice(list(model))      # a random start
    while len(out) < length:
        options = model[out[len(out) - n:]]
        if not options:
            break
        letters, weights = zip(*options.items())
        out += rng.choices(letters, weights)[0]
    return out

if __name__ == '__main__':
    text = load(sys.argv[1]) if len(sys.argv) > 1 else load()
    rng = random.Random(0)
    print('order -:', ''.join(rng.choice(ALPHABET) for _ in range(60)))
    for n in range(0, 6):
        print(f'order {n}:', generate(train(text, n), n, 60, seed=1))
