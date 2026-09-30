# Load Shakespeare and keep Shannon's 27 symbols: a-z and space.
import re

def load(path='shakespeare.txt'):
    raw = open(path).read().lower()
    return re.sub(r'[^a-z]+', ' ', raw).strip()

ALPHABET = ' abcdefghijklmnopqrstuvwxyz'
