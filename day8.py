def find(input, length):
    for i in input:
        if len(i) == length:
            return i
    return ""


def findall(input, length):
    result = []
    for i in input:
        if len(i) == length:
            result.append(i)
    return result


def main():
    with open('day8.txt', 'r') as f:
        lines = f.readlines()

    p1 = 0
    p2 = []
    for line in lines:
        for segment in line.split("|")[1].split():
            if len(segment) in (2, 3, 4, 7):
                p1 += 1

        input, output = line.split("|")
        entry = input.split()
        output = output.split()

        numbers = [""] * 10
        numbers[1] = set(find(entry, 2))
        numbers[4] = set(find(entry, 4))
        numbers[7] = set(find(entry, 3))
        numbers[8] = set(find(entry, 7))

        for candidate in findall(entry, 5):
            common_with_4 = 0
            common_with_1 = 0
            for letter in candidate:
                if letter not in numbers[4]:
                    common_with_4 += 1
                if letter in numbers[1]:
                    common_with_1 += 1
            if common_with_1 == 2:
                numbers[3] = set(candidate)
            elif common_with_4 == 3:
                numbers[2]  = set(candidate)
            else:
                numbers[5] = set(candidate)

        for candidate in findall(entry, 6):
            common_with_5 = 0
            common_with_7 = 0
            for letter in candidate:
                if letter in numbers[5]:
                    common_with_5 += 1
                if letter in numbers[7]:
                    common_with_7 += 1
            if common_with_5 == 4:
                numbers[0] = set(candidate)
            elif common_with_7 == 2:
                numbers[6] = set(candidate)
            else:
                numbers[9] = set(candidate)
        p2.append(int("".join([str(numbers.index(set(n))) for n in output])))
    print(f'part1: {p1}')
    print(f'part2: {sum(p2)}')


if __name__ == "__main__":
    main()

# 0: 6 segments -> 3 candidates [xxx-xxx]       check 4 common with 5
# 1: 2 segments -> unique       [--x--x-]   V
# 2: 5 segments -> 3 candidates [x-xxx-x]       check 2 common with 4
# 3: 5 segments -> 3 candidates [x-xx-xx]       check 2 common with 1 (&& 3 with 4?)
# 4: 4 segments -> unique       [-xxx-x-]   V
# 5: 5 segments -> 3 candidates [xx-x-xx]       check 3 common with 4
# 6: 6 segments -> 3 candidates [xx-xxxx]       check 2 common with 7
# 7: 3 segments -> unique       [x-x--x-]   V
# 8: 7 segments -> unique       [xxxxxxx]   V
# 9: 6 segments -> 3 candidates [xxxx-xx]       check 3 common with 7