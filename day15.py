import aocutils
from aocutils import a_star_grid
from aocutils import Node


def add_nodes(grid):
    new_grid = []
    for x in range(len(grid[0])):
        new_grid.append([])
        for y in range(len(grid)):
            new_grid[-1].append(Node(grid[x][y], (x,y)))
    return new_grid


def expand_grid(grid, times=5, max=9):
    new_grid = []
    xsize = len(grid[0])
    ysize = len(grid)
    for x in range(xsize * times):
        new_grid.append([])
        for y in range(ysize * times):
            if x < len(grid) and y < ysize:
                new_grid[-1].append(Node(grid[x][y], (x, y)))
            else:
                # up
                if x - xsize >= 0:
                    new_grid[-1].append(Node(new_grid[x - xsize][y].value + 1, (x, y)))
                # left
                else:
                    new_grid[-1].append(Node(new_grid[x][y-ysize].value + 1, (x, y)))
                if new_grid[x][y].value == max+1:
                    new_grid[x][y].value = 1
    return new_grid


@aocutils.timeit
def main():
    grid = aocutils.get_gridfromfile("day15.txt")

    new_grid = add_nodes(grid)
    path, cost = (a_star_grid(new_grid[0][0], new_grid[-1][-1], new_grid))
    print(f'part1: {cost[new_grid[-1][-1]]}')

    new_grid = expand_grid(grid)
    path, cost = (a_star_grid(new_grid[0][0], new_grid[-1][-1], new_grid))
    print(f'part2: {cost[new_grid[-1][-1]]}')


if __name__ == "__main__":
    main()
