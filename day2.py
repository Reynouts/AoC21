def solve(data, funcmap):
    forward = depth = aim = 0
    for command, steps in data:
        forward, depth, aim = funcmap[command](steps, forward, depth, aim)
    return forward*depth


def main():
    with open('day2.txt', 'r') as f:
        data = [(line[0], int(line[1])) for line in (l.split() for l in f)]

    funcmap = {"forward": lambda steps, forward, depth, aim: (forward+steps, depth, aim),
                  "down": lambda steps, forward, depth, aim: (forward, depth+steps, aim),
                    "up": lambda steps, forward, depth, aim: (forward, depth-steps, aim)}
    print(solve(data, funcmap))

    funcmap = {"forward": lambda steps, forward, depth, aim: (forward+steps, depth+aim*steps, aim),
                  "down": lambda steps, forward, depth, aim: (forward, depth, aim+steps),
                    "up": lambda steps, forward, depth, aim: (forward, depth, aim-steps)}
    print(solve(data, funcmap))


if __name__ == "__main__":
    main()
