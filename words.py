# The same trick with whole words instead of letters.
import random
from collections import Counter, defaultdict
from text import load

words = load().split()
nxt = defaultdict(Counter)
for a, b in zip(words, words[1:]):
    nxt[a][b] += 1

def sentence(start, length=14, seed=3):
    rng = random.Random(seed)
    out = [start]
    for _ in range(length - 1):
        opts = nxt[out[-1]]
        out.append(rng.choices(list(opts), list(opts.values()))[0])
    return ' '.join(out)

if __name__ == '__main__':
    print('after "my":', nxt['my'].most_common(5))
    print(sentence('the'))
