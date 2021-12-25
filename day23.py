import os
import msvcrt


class Amphipod:
    cost = {"A": 1, "B": 10, "C": 100, "D": 1000}

    def __init__(self, letter, position, selected):
        self.letter = letter
        self.position = position
        self.selected = selected
        self.history = {}

    def __str__(self):
        return self.letter + " " + str(self.position)

    def get_history(self):
        if self.position in self.history:
            return self.history[self.position]
        return -1

    def move_cost(self):
        return self.cost[self.letter]


def selected(amphi):
    for a in amphi:
        if a.selected:
            return a


def switch_amphi(grid, amphi, selected, score):
    next = False
    while True:
        for j, line in enumerate(grid):
            for i, c in enumerate(grid[j]):
                if next:
                    for a in amphi:
                        if a.position == (i, j):
                            selected.selected = False
                            selected.history = {}
                            a.selected = True
                            a.history[a.position] = score
                            return a
                if selected.position == (i, j):
                    next = True


def printfield(grid, amphi, tolower=True, toprint=True):
    res = ""
    for j, line in enumerate(grid):
        for i, c in enumerate(grid[j]):
            res += grid[j][i]
            for a in amphi:
                if a.position == (i, j):
                    l = a.letter
                    if a.selected and tolower:
                        l = a.letter.lower()
                    res = res[:-1] + l
                    break
        res += "\n"
    if toprint:
        print(res)
    return res


def move(grid, amphi, active, direction, score):
    heading = {"d": (1, 0), "w": (0, -1), "s": (0, 1), "a": (-1, 0)}
    new_pos = tuple([x + y for (x, y) in zip(heading[direction], active.position)])
    if grid[new_pos[1]][new_pos[0]] == ".":
        for a in amphi:
            if a.position == new_pos:
                return 0
        active.position = new_pos
        return True
    return False


def readlayout(file):
    grid = []
    amphi = []
    with open(file, 'r') as f:
        first = True
        for j, line in enumerate(f):
            grid.append([])
            for i, c in enumerate(line):
                if c != "\n":
                    if c in "ABCD":
                        grid[-1].append(".")
                        amphi.append(Amphipod(c, (i, j), first))
                        if first:
                            first = False
                    else:
                        grid[-1].append(c)
    return grid, amphi

def main():
    grid, amphi = readlayout("day23.txt")
    solution = printfield(*readlayout("day23win.txt"), False, False)

    score = 0
    active = selected(amphi)
    active.history[active.position] = score
    memento = [(score, active, active.position)]
    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    while (True):
        clearConsole()
        printfield(grid, amphi)
        if printfield (grid, amphi, False, False) == solution:
            print("You won! Thanks for playing. Total score:", score)
            return
        active = selected(amphi)
        print("Amphi selected: ", active)
        print("Total score:", score)
        print("Tab to switch amphipod, wasd to move, q to undo, b to stop")
        l = msvcrt.getch().decode('utf-8', errors='strict')
        if l == "\t":
            active = switch_amphi(grid, amphi, active, score)
            memento.append((score, active, active.position))
        elif l in "wasd":
            if move(grid, amphi, active, l, score):
                oldscore = active.get_history()
                if oldscore != -1:
                    score = oldscore
                else:

                    score += active.move_cost()
                    if active.get_history() == -1:
                        active.history[active.position] = score
        elif l == "q":
            if len(memento) > 0:
                score, active, position = memento.pop()
                active.position = position
                memento.append((score, active, active.position))
        elif l == "b":
            return


if __name__ == "__main__":
    main()
