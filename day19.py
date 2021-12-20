import re
import itertools
import numpy as np
from collections import Counter


def orientations(sc):
    for dirx, diry in itertools.permutations(range(3), 2):
        for signx, signy in itertools.product((-1, 1), (-1, 1)):
            x = np.zeros((3,))
            y = np.zeros((3,))
            x[dirx] = signx
            y[diry] = signy
            yield [[int(np.dot(x, b)), int(np.dot(y, b)),int(np.dot(np.cross(x, y), b))] for b in sc]


def findscandiff(sc1, sc2):
    for sc2 in orientations(sc2):
        diffs = []
        for i in range(len(sc1)):
            for j in range(len(sc2)):
                cx = sc1[i][0] - sc2[j][0]
                cy = sc1[i][1] - sc2[j][1]
                cz = sc1[i][2] - sc2[j][2]
                diffs.append((cx, cy, cz))
        most_common,num_most_common = Counter(diffs).most_common(1)[0]
        if num_most_common >= 12:
            return most_common, sc2
    return None, sc2


def merge(truth, scanner, scandiff):
    for s in scanner:
        nx = s[0] + scandiff[0]
        ny = s[1] + scandiff[1]
        nz = s[2] + scandiff[2]
        np = [nx, ny, nz]
        if np not in truth:
            truth.append(np)
    return truth


def main():
    with open("day19.txt", 'r') as f:
        inputs = f.read().split("\n\n")
    scanners = []
    beacons = []
    for input in inputs:
        scanners.append([])
        for line in input.split():
            numbers = list(map(int, re.findall("-?\d+", line)))
            if len(numbers) > 1:
                scanners[-1].append(numbers)
        beacons.append([False] * len(scanners[-1]))

    truth = scanners[0]

    matched = set()
    matched.add(0)
    scanner_positions = [[0, 0, 0]]
    while len(matched) != len(scanners):
        for i in range(len(scanners)):
            if i not in matched:
                scandiff, aligned_scanner = findscandiff(truth, scanners[i])
                if scandiff:
                    print(len(truth))
                    truth = merge(truth, aligned_scanner, scandiff)
                    print(len(truth))
                    matched.add(i)
                    scanner_positions.append(scandiff)
    print(scanner_positions)

    largest = 0
    for s1 in scanner_positions:
        for s2 in scanner_positions:
            manhattan = abs(s1[0] - s2[0]) + abs(s1[1] - s2[1]) + abs(s1[2] - s2[2])
            if manhattan > largest:
                largest = manhattan
    print(largest)


if __name__ == "__main__":
    main()

