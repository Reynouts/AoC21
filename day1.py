def solve(data: list[int], window: int = 1) -> int:
    return sum([1 for index, n in enumerate(data[window:], start=window) if data[index - window] < n])


def main():
    with open('day1.txt', 'r') as f:
        data = list(map(int, f.read().split()))
    print(f"Part 1: {solve(data)}")
    print(f"Part 2: {solve(data, 3)}")


if __name__ == "__main__":
    main()
