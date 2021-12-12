def main():
    with open('day10.txt', 'r') as f:
        data = f.read().splitlines()

    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    part1 = 0
    part2 = []
    incomplete = []
    points = {")": (3, 1), "]": (57, 2), "}": (1197, 3), ">": (25137, 4)}
    for line in data:
        stack = []
        errors = []
        for c in line:
            if c in pairs:
                stack.append(c)
            else:
                if pairs[stack[-1]] != c:
                    errors.append(c)
                    break
                else:
                    stack.pop(-1)
        if not errors and len(stack) > 0:
            score = 0
            for i in reversed(stack):
                score = score * 5 + points[pairs[i]][1]
            part2.append(score)
        else:
            part1 += sum([points[e][0] for e in errors])
    print(f'part1: {part1}')
    print(f'part2: {sorted(part2)[len(part2) // 2]}')


if __name__ == "__main__":
    main()
