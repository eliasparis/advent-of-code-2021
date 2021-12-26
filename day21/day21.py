from functools import lru_cache
from copy import deepcopy
from itertools import product
# Part 1: Play a practice game using the deterministic 100-sided die. The moment either player wins,
# what do you get if you multiply the score of the losing player by the number of times the die was rolled during the game?

positions = [7, 9]
scores = [0, 0]
moves = 0
dice = 1

while scores[0] < 1000 and scores[1] < 1000:
    up = 0 if moves % 2 == 0 else 1
    m = 0
    for _ in range(3):
        m += dice
        dice = dice + 1 if dice < 100 else 1

    for _ in range(m):
        np = positions[up] + 1
        positions[up] = np if np <= 10 else 1

    scores[up] += positions[up]
    moves += 3

result = min(scores) * moves
print(result)

# Part 2: Using your given starting positions, determine every possible outcome.
# Find the player that wins in more universes; in how many universes does that player win?
posibles2 = list(map(sum, product([1, 2, 3], repeat=3)))


@lru_cache(maxsize=None)
def game(player, score0, position0, score1, position1):

    if score0 >= 21:
        return 1, 0
    elif score1 >= 21:
        return 0, 1

    wins = [0]*2

    for die in posibles2:
        if player == 0:
            nposition0 = ((position0 + die - 1) % 10) + 1
            nscore0 = score0 + nposition0
            wins0, wins1 = game(1, nscore0, nposition0, score1, position1)
        else:
            nposition1 = ((position1 + die - 1) % 10) + 1
            nscore1 = score1 + nposition1
            wins0, wins1 = game(0, score0, position0, nscore1, nposition1)

        wins[0] += wins0
        wins[1] += wins1

    return wins


wins = game(0, 0, 7, 0, 9)
print(max(wins))
