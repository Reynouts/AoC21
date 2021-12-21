import aocutils


def get_binary_sliding_window(middle, cells, outer):
    result = ""
    for h in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)):
        pos = middle[0] + h[0], middle[1] + h[1]
        if pos in cells:
            result += cells[pos]
        else:
            result += outer
    return result


def evolve(cells, frame, outer, algo, expand):
    return {(i, j): algo[int(get_binary_sliding_window((i, j), cells, outer), 2)]
                for i in range(-expand, frame[0]+expand)
                for j in range(-expand, frame[1]+expand)}


@aocutils.timeit
def main():
    with open("day20.txt", 'r') as f:
        algo, input = f.read().replace("#", "1").replace(".", "0").split("\n\n")
        input = input.splitlines()
    cells = {(y, x): cell for y, line in enumerate(input) for x, cell in enumerate(line)}
    frame = [len(input), len(input[0])]
    outer = "0"
    for i in range(50):
        cells = evolve(cells, frame, outer, algo, i+1)
        if algo[0] == "1" and algo[-1] == "0":
            outer = str((int(outer) + 1) % 2)
        elif algo[0] == "1":
            outer = "1"
        else:
            outer = "0"
        if i == 1:
            print("part1:", sum(map(int, cells.values())))
    print("part2:", sum(map(int, cells.values())))


if __name__ == "__main__":
    main()
