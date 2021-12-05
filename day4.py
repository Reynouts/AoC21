import numpy as np


def parse(data):
    header = data[0]
    numbers = list(map(int, header.split(",")))
    boards = []
    for line in data[1:]:
        if len(line) < 5:
            boards.append([])
        else:
            boards[-1].append(list (map(int, line.rstrip().split())))
    return numbers, boards


def check_board(board):
    return any(np.all((np.array(board) == -1), axis=0)) or any(np.all((np.array(board) == -1), axis=1))


def cycle(numbers, boards, win=0):
    checked = []
    for n in numbers:
        for index, board in enumerate(boards):
            if index not in checked:
                boards[index] = [[p if p!=n else -1 for p in s] for s in board]
                if check_board(boards[index]):
                    if len(checked) == win:
                        counter = 0
                        for row in boards[index]:
                            for e in row:
                                if e != -1:
                                    counter += e
                        return counter * n
                    else:
                        checked.append(index)
    return -1


def main():
    with open('day4.txt', 'r') as f:
        data = f.readlines()
    numbers, boards = parse(data)
    print(f"Part1: {cycle(numbers,boards, 0)}")
    print(f"Part2: {cycle(numbers,boards, len(boards)-1)}")


if __name__ == "__main__":
    main()
