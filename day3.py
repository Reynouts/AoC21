import numpy as np


def part1(data):
    gamma = ''.join(['1' if i > (data.shape[0]/2) else '0' for i in data.sum(axis=0)])
    epsilon = int(''.join('1' if x == '0' else '0' for x in gamma), 2)
    gamma = int(gamma, 2)
    return gamma*epsilon


def part2(data):
    oxygen = filter_columns(data, 1)
    scrubber = filter_columns(data, 0)
    return oxygen*scrubber


def filter_columns(data, target, index=0):
    if index >= data.shape[1]:
        return 0
    e = target
    if data.sum(axis=0)[index] >= data.shape[0]/2:
        e = 1 - e
    data = data[data[:, index] == e]
    if data.shape[0] == 1:
        return int(''.join(map(str, data[0])), 2)
    return filter_columns(data, target, index+1)


def main():
    data = np.genfromtxt('day3.txt', delimiter=1, dtype=int)
    print(f"Part 1: {part1(data)}")
    print(f"part 2: {part2(data)}")


if __name__ == "__main__":
    main()