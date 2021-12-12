import os
from aocd import get_data
import time


def get_input(day, token="\n"):
    "Open input file of corresponding day. Returns a list of strings"
    return get_data(day=day).split(token)


def get_file(day, token="\n"):
    with open('day{}.txt'.format(day), 'r') as f:
        return f.read().split(token)


def write_input(day):
    with open('day{}.txt'.format(day), 'w') as f:
        f.write(get_data(day=day))


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def get_dictgridfromfile(file):
    cells = {}
    with open(file, 'r') as f:
        for i, line in enumerate(f.readlines()):
            for j, cell in enumerate(line):
                if cell != "\n":
                    cells[(i, j)] = int(cell)
    return cells


def get_neighbours(cell, cells, diag=True):
    neighbours = []
    heading = ((1, 0), (-1, 0), (0, 1), (0, -1))
    if diag:
        heading = heading + ((1, 1), (-1, -1), (-1, 1), (1, -1))
    for h in heading:
        pos = cell[0] + h[0], cell[1] + h[1]
        if pos in cells:
            neighbours.append(pos)
    return neighbours


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result

    return timed
