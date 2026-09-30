# 1950: how a machine could play chess. Minimax on tic-tac-toe.
from functools import lru_cache

LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
seen = 0

def winner(b):
    for i, j, k in LINES:
        if b[i] != '.' and b[i] == b[j] == b[k]:
            return b[i]
    return None

@lru_cache(None)
def minimax(b, player):
    global seen
    seen += 1
    w = winner(b)
    if w: return 1 if w == 'X' else -1       # score for X
    if '.' not in b: return 0                # draw
    scores = [minimax(b[:i] + player + b[i+1:], 'O' if player == 'X' else 'X')
              for i in range(9) if b[i] == '.']
    return max(scores) if player == 'X' else min(scores)

if __name__ == '__main__':
    print('perfect play value:', minimax('.' * 9, 'X'))
    print('positions examined:', seen)
