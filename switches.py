# 1937: Shannon's master's thesis. Switches do logic; logic does math.

def AND(a, b): return a & b      # two switches in series
def OR(a, b):  return a | b      # two switches in parallel
def NOT(a):    return 1 - a      # a relay that opens when powered
def XOR(a, b): return OR(AND(a, NOT(b)), AND(NOT(a), b))

def full_adder(a, b, carry):
    s = XOR(XOR(a, b), carry)
    carry = OR(AND(a, b), AND(carry, XOR(a, b)))
    return s, carry

def add(x, y, bits=4):
    out, carry = 0, 0
    for i in range(bits):              # right to left, like on paper
        a, b = (x >> i) & 1, (y >> i) & 1
        s, carry = full_adder(a, b, carry)
        out |= s << i
    return out | carry << bits

if __name__ == '__main__':
    print('5 + 3 =', add(5, 3))
    print('0101 + 0011 =', format(add(5, 3), '04b'))
