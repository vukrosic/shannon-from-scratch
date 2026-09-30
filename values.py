# Run every demo once and save the numbers the video shows.
import heapq, json, random, zlib
from collections import Counter
from math import log2
import switches, surprise, markov, words, predict, huffman, channel, hamming, secret, chess
from text import load, ALPHABET

V = {}
text = load()
V['chars'] = len(text)
cnt = Counter(text)
V['freq'] = {c: round(cnt[c] / len(text), 5) for c in ALPHABET}
V['H_uniform'] = round(log2(27), 3)
V['H_letters'] = round(surprise.entropy([cnt[c] / len(text) for c in ALPHABET]), 3)
V['add'] = switches.add(5, 3)
V['coin'] = {'fair': 1.0, '90': round(surprise.entropy([.9, .1]), 3), '99': round(surprise.entropy([.99, .01]), 3)}
V['coin_curve'] = [round(surprise.entropy([p, 1 - p]), 4) for p in [i / 40 for i in range(41)]]
V['die'] = round(surprise.surprise(1 / 6), 3)
rng = random.Random(0)
V['samples'] = {'rand': ''.join(rng.choice(ALPHABET) for _ in range(60))}
for n in range(0, 6):
    V['samples'][str(n)] = markov.generate(markov.train(text, n), n, 60, seed=1)
V['after_th'] = markov.train(text, 2)['th'].most_common(6)
V['after_q'] = markov.train(text, 1)['q'].most_common(3)
V['after_my'] = words.nxt['my'].most_common(5)
V['word_sentence'] = words.sentence('the')
V['xent'] = [round(predict.cross_entropy(n), 3) for n in range(0, 7)]
code = huffman.huffman(cnt)
V['huff'] = code

# the same merges huffman() makes, in order, for the tree animation: [left group, right group, weight]
heap = [(n, i, c) for i, (c, n) in enumerate(cnt.items())]
heapq.heapify(heap); merges = []
while len(heap) > 1:
    n1, i1, a = heapq.heappop(heap); n2, i2, b = heapq.heappop(heap)
    merges.append([a, b, n1 + n2]); heapq.heappush(heap, (n1 + n2, i2, a + b))
V['huff_merges'] = merges
V['counts'] = dict(cnt)
bits = sum(len(code[c]) for c in text)
V['huff_bpl'] = round(bits / len(text), 3)
V['huff_bytes'] = bits // 8
V['fixed_bytes'] = 5 * len(text) // 8
V['raw_bytes'] = len(text)
z = len(zlib.compress(text.encode(), 9))
V['zlib_bytes'] = z
V['zlib_bpl'] = round(z * 8 / len(text), 3)
r = random.Random(0)
msg = [r.randint(0, 1) for _ in range(200000)]
V['rep'] = []
for n in (1, 3, 5, 7, 9, 11):
    got = channel.vote(channel.noisy(channel.repeat(msg, n), 0.1, r), n)
    V['rep'].append([n, round(1 / n, 4), round(channel.error_rate(msg, got), 5)])
V['capacity'] = round(channel.capacity(0.1), 4)
sent = hamming.encode([1, 0, 1, 1]); got = sent[:]; got[4] ^= 1
V['ham'] = {'sent': ''.join(map(str, sent)), 'got': ''.join(map(str, got)), 'pos': hamming.decode(got)[1]}
V['pad'] = {'cipher': secret.cipher.hex(), 'key': secret.key.hex()}
V['ttt_value'] = chess.minimax('.' * 9, 'X')
V['ttt_positions'] = chess.seen
json.dump(V, open('values.json', 'w'), indent=1)
print(json.dumps({k: V[k] for k in ('H_letters', 'xent', 'huff_bpl', 'zlib_bpl', 'rep', 'capacity', 'after_th', 'after_q')}, indent=None))
