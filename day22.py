import aocutils
from collections import defaultdict
import re


class Cube:
    def __init__(self, xstart, xend, ystart, yend, zstart, zend, switch=True):
        self.xstart = xstart
        self.xend = xend
        self.ystart = ystart
        self.yend = yend
        self.zstart = zstart
        self.zend = zend
        self.switch = switch

    def __str__(self):
        return ", ".join(list(map(str, (self.xstart, self.xend, self.ystart, self.yend, self.zstart, self.yend))))


def cube_intersect(c1, c2):
    xstart = max(c1.xstart, c2.xstart)
    ystart = max(c1.ystart, c2.ystart)
    zstart = max(c1.zstart, c2.zstart)
    xend = min(c1.xend, c2.xend)
    yend = min(c1.yend, c2.yend)
    zend = min(c1.zend, c2.zend)
    if xstart <= xend and ystart <= yend and zstart <= zend:
        return Cube(xstart, xend, ystart, yend, zstart, zend)


@aocutils.timeit
def main():
    with open("day22.txt", 'r') as f:
        lines = f.read().splitlines()
    cubes = defaultdict(bool)
    for line in lines:
        xstart, xend, ystart, yend, zstart, zend = list(map(int, re.findall("-?\d+", line)))
        for x in range(max(-50,xstart), min(xend, 50)+1):
            for y in range(max(-50,ystart), min(yend, 50)+1):
                for z in range(max(-50,zstart), min(zend, 50)+1):
                    if "on" in line:
                        cubes[(x,y,z)] = True
                    else:
                        cubes[(x,y,z)] = False
    print(sum([1 if cubes[c] else 0 for c in cubes]))

    cubes = set()
    for index, line in enumerate(lines):
        xstart, xend, ystart, yend, zstart, zend = list(map(int, re.findall("-?\d+", line)))
        c1 = Cube(xstart, xend, ystart, yend, zstart, zend, "on" in line)
        for c2 in cubes.copy():
            if cube_intersect(c1, c2):
                intercube = cube_intersect(c1, c2)
                if c2.switch:
                    intercube.switch = False
                cubes.add(intercube)
        if c1.switch:
            cubes.add(c1)

    count = 0
    for c in cubes:
        points = (c.xend-c.xstart+1) * (c.yend - c.ystart+1) * (c.zend - c.zstart+1)
        if not c.switch:
            points *= -1
        count += points

    print(count)


if __name__ == "__main__":
    main()
