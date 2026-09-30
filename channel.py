# 1948: sending bits through noise. Every bit flips with chance p.
import random
from math import log2

def noisy(bits, p, rng):
    return [b ^ (rng.random() < p) for b in bits]

def capacity(p):
    h = -p * log2(p) - (1 - p) * log2(1 - p)
    return 1 - h            # useful bits per bit sent

def repeat(bits, n):
    return [b for b in bits for _ in range(n)]

def vote(bits, n):
    return [int(sum(bits[i:i + n]) > n // 2)
            for i in range(0, len(bits), n)]

def error_rate(a, b):
    return sum(x != y for x, y in zip(a, b)) / len(a)

if __name__ == '__main__':
    rng = random.Random(0)
    msg = [rng.randint(0, 1) for _ in range(200000)]
    p = 0.1
    for n in (1, 3, 5, 7, 9, 11):
        got = vote(noisy(repeat(msg, n), p, rng), n)
        print(f'repeat x{n:<2}: errors {error_rate(msg, got):.4%}'
              f'  rate {1 / n:.3f}')
    print('capacity p=0.1:', round(capacity(p), 3), 'bits per bit')
