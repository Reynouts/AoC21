def get_binary_sliding_window(middle, cells, outer):
    result = ""
    heading = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1))
    for h in heading:
        pos = middle[0] + h[0], middle[1] + h[1]
        if pos in cells:
            result += cells[pos]
        else:
            result += outer
    return result


def evolve(cells, frame, outer, algo):
    new_cells = {}
    for i in range(frame[0] - 1, frame[1] + 1):
        for j in range(frame[2] - 1, frame[3] + 1):
            new_cells[(i, j)] = algo[int(get_binary_sliding_window((i, j), cells, outer), 2)]
    return new_cells, [frame[0] - 1, frame[1] + 1, frame[2] - 1, frame[3] + 1]


def main():
    with open("day20.txt", 'r') as f:
        algo, input = f.read().split("\n\n")
    input = input.splitlines()
    algo = ["1" if c == "#" else "0" for c in algo]

    cells = {}
    for i, line in enumerate(input):
        for j, cell in enumerate(line):
            if cell != "\n":
                if cell == "#":
                    cells[(i, j)] = "1"
                else:
                    cells[(i, j)] = "0"

    frame = [0, len(input), 0, len(input[0])]
    outer = "0"
    for i in range(50):
        cells, frame = evolve(cells, frame, outer, algo)
        if algo[0] == "1" and algo[-1] == "0":
            outer = str((int(outer)+1)%2)
        elif algo[0] == "#":
            outer = "1"
        else:
            outer = "0"
        if i == 1:
            print("part1:", sum(map(int, cells.values())))
    print("part2:", sum(map(int, cells.values())))


if __name__ == "__main__":
    main()
