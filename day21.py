from functools import lru_cache
from itertools import product
from collections import defaultdict
import aocutils


def detdice():
    dice = -1
    while True:
        dice += 3
        yield dice * 3


def play_det(pawns):
    scores = [0, 0]
    index = 0
    for i, steps in enumerate(detdice()):
        pawns[index] = (pawns[index] + steps) % 10
        scores[index] += pawns[index]
        if pawns[index] == 0:
            scores[index] += 10
        if scores[index] >= 1000:
            return(scores[(index + 1) % 2] * (i * 3 + 3))
        index = (index + 1) % 2


@lru_cache(maxsize=None)
def play(pos1, score1, pos2, score2):
    if score2 >= 21:
        return 0, 1
    win1 = win2 = 0
    for o in outcomes:
        new_pos1 = (pos1 + o) % 10
        new_score1 = score1 + new_pos1
        if new_pos1 == 0:
            new_score1 += 10
        _win2, _win1 = play(pos2, score2, new_pos1, new_score1)
        win1 += _win1*outcomes[o]
        win2 += _win2*outcomes[o]
    return win1, win2


outcomes = defaultdict(int)
def main():
    numbers = aocutils.get_digits_from_input(21)
    print("part1:", play_det([numbers[1], numbers[3]]))

    for i in (product([1, 2, 3], repeat=3)):
        outcomes[sum(i)] += 1
    print("part2:",max(play(numbers[1], 0, numbers[3], 0)))


if __name__ == "__main__":
    main()