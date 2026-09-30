# 1949: the one-time pad. A random key as long as the message.
import random

def xor(data, key):
    return bytes(d ^ k for d, k in zip(data, key))

message = b'ATTACK AT DAWN'
key = random.Random(1949).randbytes(len(message))  # use real dice
cipher = xor(message, key)

if __name__ == '__main__':
    print('cipher :', cipher.hex())
    print('decrypt:', xor(cipher, key).decode())
    other = xor(cipher, b'RETREAT AT TEN')     # another possible key
    print('other key:', xor(cipher, other).decode())
