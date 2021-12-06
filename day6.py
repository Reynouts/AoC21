import re
from collections import deque


def cycle(steps, population):
    for _ in range(steps):
        oldies = population[0]
        population.rotate(-1)
        population[6] += oldies
    return sum(population)


def main():
    with open('day6.txt', 'r') as f:
        fishes = list(map(int, re.findall("\d+", f.read())))
    population = deque([0] * 9)
    for fish in fishes:
        population[fish] += 1

    print(f"part1: {cycle(80, population.copy())}")
    print(f"part2: {cycle(256, population)}")


if __name__ == "__main__":
    main()
