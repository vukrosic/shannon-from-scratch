# Hamming(7,4): 4 data bits + 3 check bits. Fixes any single flip.

def encode(d):
    a, b, c, e = d
    return [a ^ b ^ e, a ^ c ^ e, a, b ^ c ^ e, b, c, e]

def decode(r):
    s1 = r[0] ^ r[2] ^ r[4] ^ r[6]
    s2 = r[1] ^ r[2] ^ r[5] ^ r[6]
    s3 = r[3] ^ r[4] ^ r[5] ^ r[6]
    pos = s1 + 2 * s2 + 4 * s3          # 0 = no error
    if pos:
        r = r[:]
        r[pos - 1] ^= 1                 # flip it back
    return [r[2], r[4], r[5], r[6]], pos

if __name__ == '__main__':
    sent = encode([1, 0, 1, 1])
    print('send   :', ''.join(map(str, sent)))
    got = sent[:]
    got[4] ^= 1                         # noise flips bit 5
    print('receive:', ''.join(map(str, got)))
    data, pos = decode(got)
    print('checks say position', pos, '-> data', ''.join(map(str, data)))
