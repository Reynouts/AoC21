import re
from itertools import permutations


def reduce(snail):
    exploded = splitted = True
    while (exploded or splitted):
        exploded, snail = explode(snail)
        if not exploded:
            splitted, snail = split(snail)
    return (snail)


def explode(testsnail):
    depth = i = 0
    lastnumberindex = -1
    newsnail = ""
    while i < len(testsnail):
        if testsnail[i] == "[":
            depth += 1
        elif testsnail[i] == "]":
            depth -= 1
        elif testsnail[i].isdigit():
            lastnumberindex = i

        # This thing needs to explode! Too deep!
        if depth == 5:
            offset = 4
            while testsnail[i + offset] != "]":
                offset += 1
            n1, n2 = re.findall("\d+", testsnail[i:i + offset + 1])
            i += offset + 1
            depth -= 1

            # search first number on the left and add first number of the exploding pair
            if lastnumberindex >= 0:
                lastnumber = testsnail[lastnumberindex]
                extendedlastnumber = lastnumberindex - 1
                while testsnail[extendedlastnumber].isdigit():
                        lastnumber = testsnail[extendedlastnumber] + lastnumber
                        extendedlastnumber -= 1
                newnumber = str(int(lastnumber) + int(n1))
                newsnail = newsnail[:lastnumberindex - len(lastnumber) + 1] + newnumber + newsnail[lastnumberindex + 1:]

            # leave a naked zero in place of the exploded pair
            newsnail += "0"

            # search first number on the right and add second number of pair
            while i < len(testsnail) and not testsnail[i].isdigit():
                newsnail += testsnail[i]
                i += 1
            if i == len(testsnail):
                break
            nextnumber = testsnail[i]
            i += 1
            while testsnail[i].isdigit():
                nextnumber += testsnail[i]
                i += 1
            newsnail += str(int(n2) + int(nextnumber)) + testsnail[i:]
            return True, newsnail
        newsnail += testsnail[i]
        i += 1
    return False, newsnail


def split(testsnail):
    query = re.search("\d{2,}", testsnail)
    if query:
        begin, end = query.span()
        number = query[0]
        newsnail = testsnail[:begin] + "["
        number = int(number)
        one = second = number // 2
        if (number % 2) != 0:
            second = one + 1
        newsnail += str(one) + ","
        newsnail += str(second) + "]"
        newsnail += testsnail[end:]
        return True, newsnail
    return False, testsnail


def magnitude(snail):
    query = True
    while query:
        query = re.search(r"\[(\d+),(\d+)\]", snail)
        if query:
            start, end = query.span()
            n = 3 * int(query.group(1)) + 2 * int(query.group(2))
            snail = snail[:start] + str(n) + snail[end:]
    return snail


def main():
    with open("day18.txt", 'r') as f:
        lines = f.read().splitlines()

    homework = lines[0]
    for line in lines[1:]:
        homework = reduce("[" + homework + ',' + line + "]")
    print("part1:", magnitude(homework))

    maxmag = 0
    for i in permutations(range(0, len(lines)), 2):
        homework = reduce("[" + lines[i[0]] + ',' + lines[i[1]] + "]")
        magni = int(magnitude(homework))
        if magni > maxmag:
            maxmag = magni
    print("part2:", maxmag)


if __name__ == "__main__":
    main()
