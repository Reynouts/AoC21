import re
from collections import defaultdict


def line_points(x1, y1, x2, y2):
    points = []
    if x1 == x2:
        for i in range(min(y1, y2), max(y1,y2)+1):
            points.append((x1, i))
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1,x2)+1):
            points.append((i, y1))
    else:
        if x2 < x1:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        y = float(y1)
        for x in range(x1, x2+1):
            if y.is_integer():
                points.append((x, int(y)))
            y += (x2-x1) / (y2-y1)
    return points


def main():
    with open('day5.txt', 'r') as f:
        data = f.readlines()

    mp = defaultdict(int)
    for line in data:
        x1, y1, x2, y2 = list(map(int, re.findall("\d+", line)))
        points = line_points(x1, y1, x2, y2)
        for point in points:
            mp[point] += 1
    print(sum([1 if mp[k] > 1 else 0 for k in mp]))


if __name__ == "__main__":
    main()
