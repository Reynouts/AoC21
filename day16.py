import aocutils
from math import prod

versions =[]


def getliteral(package, offset):
    keepreading = True
    literal = ""
    while(keepreading):
        if package[offset] == "0":
            keepreading = False
        literal += package[offset+1:offset+5]
        offset += 5
    return int(literal, 2), offset


def decode_package(stream):
    global versions
    if not "1" in stream:
        return 0, len(stream), -99
    version = int(stream[:3],2)
    versions.append(version)
    id = int(stream[3:6],2)
    offset = 6
    if id == 4:
        literal, offset = getliteral(stream, offset)
    else:
        length_type_id = int(stream[offset])
        values = []
        if length_type_id == 0:
            subpackets_length = int(stream[offset+1:offset+16],2)
            offset += 16
            bitsseen = 0
            while bitsseen < subpackets_length:
                v, read, value = decode_package(stream[offset::])
                bitsseen += read
                offset = offset+read
                if value != -99:
                    values.append(value)
        else:
            subpackets_amount = int(stream[offset + 1:offset + 12], 2)
            offset = offset + 12
            for _ in range(subpackets_amount):
                v, read, value = decode_package(stream[offset::])
                offset += read
                if value != -99:
                    values.append(value)
    if id == 0:
        result = sum(values)
    if id == 1:
        result = prod(values)
    if id == 2:
        result = min(values)
    if id == 3:
        result = max(values)
    if id == 4:
        result = literal
    if id == 5:
        result = int(values[0] > values[1])
    if id == 6:
        result = int(values[0] < values[1])
    if id == 7:
        result = int(values[0] == values[1])
    return version, offset, result


def main():
    with open("day16.txt", 'r') as f:
        hex = f.read().strip()
    package = (bin(int(hex, 16))[2:]).zfill(len(hex) * 4)
    result = decode_package(package)
    print("part1:", sum(versions))
    print("part2:", result[-1])


if __name__ == "__main__":
    main()
