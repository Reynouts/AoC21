from collections import defaultdict


def template_to_dict(template):
    pairdict = defaultdict(int)
    for i in range(len(template)-1):
        pairdict[template[i:i+2]] += 1
    return pairdict


def cycledict(rules, pairdict):
    olddict = pairdict.copy()
    for e in olddict:
        pairdict[e[0] + rules[e]] += olddict[e]
        pairdict[rules[e] + e[1]] += olddict[e]
        pairdict[e] -= olddict[e]
    return pairdict


def calc(pairdict, template):
    letters = defaultdict(int)
    for i in pairdict:
        letters[i[0]] += pairdict[i]
        letters[i[1]] += pairdict[i]
    letters[template[0]] += 1
    letters[template[-1]] += 1
    for i in letters:
        letters[i] = letters[i]//2
    return max(letters.values()) - min(letters.values())


def main():
    rules = {}
    with open('day14.txt', 'r') as f:
        lines = f.read().splitlines()
        template = lines[0]
        for line in lines[2:]:
            key, val = line.strip().split(' -> ')
            rules[key] = val

    pairdict = template_to_dict(template)
    for c in range(1000000000 ):
        pairdict = cycledict(rules, pairdict)
        if c == 9:
            print(f"part1: {calc(pairdict, template)}")
    print(f"part2: {calc(pairdict, template)}")


if __name__ == "__main__":
    main()