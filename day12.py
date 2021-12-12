from collections import defaultdict


def count_paths(start, end, graph, max_visits, visited):
    if start == end:
        return 1
    count = 0
    if (start not in visited or
        (all(x < max_visits for x in visited.values()) and start != "start")) \
            or start.isupper():
        if start.islower():
            if start not in visited:
                visited[start] = 1
            else:
                visited[start] += 1
        for n in graph[start]:
            count += count_paths(n, end, graph, max_visits, visited.copy())
    else:
        return 0
    return count


def main():
    graph = defaultdict(list)
    with open('day12.txt', 'r') as f:
        for edge in f.read().splitlines():
            frm, to = edge.split("-")
            graph[frm].append(to)
            graph[to].append(frm)
    print(f'part1: {count_paths("start", "end", graph, 1, {})}')
    print(f'part2: {count_paths("start", "end", graph, 2, {})}')


if __name__ == "__main__":
    main()
