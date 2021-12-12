import aocutils


def evolve(cell, cells, flashed):
    neighbours = aocutils.get_neighbours(cell, cells)
    for n in neighbours:
        if n not in flashed:
            cells[n] += 1
            if cells[n] > 9:
                flashed.add(n)
                cells, flashed = evolve(n, cells, flashed)
    return cells, flashed


def cycle(cells):
    flashed = set()
    for cell in cells:
        if cell not in flashed:
            cells[cell] += 1
            if cells[cell] > 9:
                flashed.add(cell)
                cells, flashed = evolve(cell, cells, flashed)
    for cell in cells:
        if cells[cell] > 9:
            cells[cell] = 0
    return cells, flashed


def main():
    cells = aocutils.get_dictgridfromfile("day11.txt")

    count = 0
    for i in range(10**10):
        cells, flashed = cycle(cells)
        count += len(flashed)
        if i == 99:
            print(f"part1: {count}")
        if len(flashed) == len(cells):
            print (f"part2: {i+1}")
            break


if __name__ == "__main__":
    main()
