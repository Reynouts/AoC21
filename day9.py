from collections import deque
from math import prod


def get_neighbours(cell, cells):
    neighbours = []
    for h in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if (cell[0] + h[0], cell[1] + h[1]) in cells:
            neighbours.append((cell[0] + h[0], cell[1] + h[1]))
    return neighbours


def basinsize(cell, cells):
    visited = set()
    visited.add(cell)
    queue = deque()
    queue.append(cell)

    while queue:
        s = queue.pop()
        for neighbour in get_neighbours(s, cells):
            if neighbour not in visited and cells[neighbour] != 9:
                visited.add(neighbour)
                queue.append(neighbour)
    return len(visited)


def main():
    cells = {}
    with open('day9.txt', 'r') as f:
        for i, line in enumerate(f.readlines()):
            for j, cell in enumerate(line):
                if cell != "\n":
                    cells[(i, j)] = int(cell)

    candidates = []
    for cell in cells:
        candidate = True
        for n in get_neighbours(cell, cells):
            if cells[n] <= cells[cell]:
                candidate = False
        if candidate:
            candidates.append(cell)
    print(sum([cells[c] + 1 for c in candidates]))

    basins = sorted([basinsize(c, cells) for c in candidates])
    print(prod(basins[-3::]))


if __name__ == "__main__":
    main()
