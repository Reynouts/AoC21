import re
from itertools import product


def checkvarcode(varcode, modvars, endvars):
    n = z = 0
    rescode = []
    for i in range(14):
        if modvars[i] > 0:
            rescode.append(varcode[n])
            z = (z * 26) + varcode[n] + endvars[i]
            n += 1
        else:
            rescode.append((z % 26) + modvars[i])
            if rescode[-1] < 1 or rescode[-1] > 9:
                return None
            z = z // 26
    return "".join([str(c) for c in rescode])


def solve(modvars, endvars, start, end, order):
    varcodes = product(range(start, end, order), repeat=7)
    for varcode in varcodes:
        code = checkvarcode(varcode, modvars, endvars)
        if code:
            return code


def main():
    modvars = []
    endvars = []
    with open("day24.txt", 'r') as f:
        for line in f.readlines():
            if "inp" in line:
                count = 1
            else:
                if count == 5 and "add" in line:
                    modvars.append(int(re.findall("-?\d+", line)[0]))
                if count == 15 and "add" in line:
                    endvars.append(int(re.findall("-?\d+", line)[0]))
                count += 1

    print("part1:",solve(modvars, endvars, 9, 0, -1))
    print("part2:",solve(modvars, endvars, 1, 10, 1))



if __name__ == "__main__":
    main()