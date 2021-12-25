import aocutils


def cycle(cells, width, height):
    fish = {">": (0,1), "v": (1,0)}
    for c in ">v":
        new_cells = {}
        h = fish[c]
        for cell in cells:
            if cells[cell] == c:
                if ((cell[0]+h[0])%height, (cell[1]+h[1])%width) not in cells:
                    new_cells[((cell[0]+h[0])%height, (cell[1]+h[1])%width)] = cells[cell]
                else:
                    new_cells[cell] = cells[cell]
            else:
                new_cells[cell] = cells[cell]
        if c == ">":
            cells = new_cells.copy()
    return new_cells


def str_griddict(griddict, frame, default="."):
    res = ""
    for i in range(frame[0], frame[1]):
        for j in range(frame[2], frame[3]):
            if (i, j) in griddict:
                res += griddict[(i, j)]
            else:
                res += default
        res += "\n"
    return res


@aocutils.timeit
def main():
    cells = {}
    height = 0
    width = 0
    with open("day25.txt", 'r') as f:
        for i, line in enumerate(f.readlines()):
            width = 0
            for j, cell in enumerate(line):
                if cell != "\n":
                    width += 1
                    if cell in ">v":
                        cells[(i, j)] = cell
            height += 1

    frame = (0, width+1, 0, height+1)
    state = str_griddict(cells, frame)
    for i in range(10**10):
        cells = cycle(cells.copy(), width, height)
        new_state = str_griddict(cells, frame)
        if new_state == state:
            print("part1:", i+1)
            break
        else:
            state = new_state


if __name__ == "__main__":
    main()
