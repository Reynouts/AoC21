import re


def shoot(vx, vy, target):
    x = y = 0
    maxy = 0
    while x < target[1] and y > target[2]:
        x += vx
        y += vy
        if y > maxy:
            maxy = y
        if target[0] <= x <= target[1] and target[2] <= y <= target[3]:
            return True, maxy
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        else:
            vx = 0
        vy -= 1
    return False, maxy


def main():
    with open("day17.txt", 'r') as f:
        target = list(map(int, re.findall("-?\d+", f.read())))
    heights = []
    for vx in range(0, target[1]+1):
        for vy in range(target[2], target[2]*-1):
            hit, height = shoot(vx, vy, target)
            if hit:
                heights.append(height)
    print("part1:",max(heights))
    print("part2:",len(heights))


if __name__ == "__main__":
    main()
