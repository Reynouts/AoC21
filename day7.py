import re
import statistics


def fuel(crabs, goal, cost):
    return int(sum((cost(abs(crab - goal)) for crab in crabs)))


def main():
    with open('day7.txt', 'r') as f:
        crabs = list(map(int, re.findall("\d+", f.read())))
    print(f"part1: {fuel(crabs, statistics.median(crabs), lambda x: x)}")
    print(f"part2: {min((fuel(crabs, goal, lambda x: ((x**2)+x)/2) for goal in range(len(crabs))))}")


if __name__ == "__main__":
    main()
