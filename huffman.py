# Compression: frequent letters get short codes (Huffman, 1952).
import heapq, zlib
from collections import Counter
from text import load

def huffman(counts):
    heap = [(n, i, c) for i, (c, n) in enumerate(counts.items())]
    heapq.heapify(heap)
    code = {c: '' for c in counts}
    groups = {c: [c] for c in counts}
    while len(heap) > 1:
        n1, i1, a = heapq.heappop(heap)    # two rarest
        n2, i2, b = heapq.heappop(heap)
        for c in groups[a]: code[c] = '0' + code[c]
        for c in groups[b]: code[c] = '1' + code[c]
        groups[a + b] = groups[a] + groups[b]
        heapq.heappush(heap, (n1 + n2, i2, a + b))
    return code

if __name__ == '__main__':
    text = load()
    code = huffman(Counter(text))
    for c in ' etoa':
        print(repr(c), code[c])
    print("'z'", code['z'], "'q'", code['q'])
    bits = sum(len(code[c]) for c in text)
    print('fixed 5 bits :', 5 * len(text) // 8, 'bytes')
    print('huffman      :', bits // 8, 'bytes',
          round(bits / len(text), 2), 'bits per letter')
    z = len(zlib.compress(text.encode(), 9))
    print('zlib         :', z, 'bytes',
          round(z * 8 / len(text), 2), 'bits per letter')
