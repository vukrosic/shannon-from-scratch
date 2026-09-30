# 1948: information is surprise. Entropy is the average surprise.
from math import log2

def surprise(p):
    return -log2(p)                    # bits

def entropy(probs):
    return sum(p * surprise(p) for p in probs if p > 0)

if __name__ == '__main__':
    print('coin flip    :', surprise(1 / 2), 'bit')
    print('one of 8     :', surprise(1 / 8), 'bits')
    print('die roll     :', round(surprise(1 / 6), 2), 'bits')
    print('fair coin H  :', entropy([0.5, 0.5]))
    print('90/10 coin H :', round(entropy([0.9, 0.1]), 3))
    print('99/1 coin H  :', round(entropy([0.99, 0.01]), 3))
