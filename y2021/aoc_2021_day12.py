from __future__ import annotations

from collections import defaultdict

puzzle_input = 'pq-GX\nGX-ah\nmj-PI\ney-start\nend-PI\nYV-mj\nah-iw\nte-GX\nte-mj\nZM-iw\nte-PI\nah-ZM\ney-te\nZM-end\nend-mj\nte-iw\nte-vc\nPI-pq\nPI-start\npq-ey\nPI-iw\nah-ey\npq-iw\npq-start\nmj-GX'.strip()
test_input = 'start-A\nstart-b\nA-c\nA-b\nb-d\nA-end\nb-end'.strip()

def parse_lines(lines: str) -> dict[str, list[str]]:
    # get a 'graph' of all the caves: the dictionary version of the puzzle input (bi-directional)
    paths = defaultdict(list)
    for line in lines.split('\n'):
        start, end = line.split('-')
        paths[start].append(end)
        paths[end].append(start)
    return dict(paths)

def sort_graph(graph: dict[str, list[str]]) -> dict[str, list[str]]:
    # sort the graph values by name (start is always first, end is always last)
    # e.g. ['end', 'C', 'd', 'b', 'start'] -> ['start', 'b', 'C', 'd', 'end']
    # this is purely for readability during debugging
    for key, value in graph.items():
        graph[key] = sorted(value, key=lambda x: chr(0x10ffff if x == 'end' else 0) if x in {'start', 'end'} else x.lower())
    return graph

def find_all_paths_part1(graph: dict, start: str, end: str, seen: set[str]) -> list[tuple[str]]:
    paths = []
    if start.islower():
        seen.add(start)
    for possible in graph[start]:
        if possible in seen:
            continue
        if possible == end:
            paths.append((start, end))
        recursive = find_all_paths_part1(graph, possible, end, seen.copy())
        paths.extend((start,) + path for path in recursive)
    return paths

def _can_we_access_cave(cave: str, seen: dict[str, int]):
    if cave.isupper():
        return True
    if cave == 'start':
        return False
    return not (cave in seen and max(seen.values(), default=0) == 2)

def find_all_paths_part2(graph: dict, start: str, end: str, seen: defaultdict[str, int]) -> list[tuple[str]]:
    paths = []
    if start == 'end':
        return paths
    seen[start] += 1 if start.islower() else 0
    for possible in graph[start]:
        if not _can_we_access_cave(possible, seen):
            continue
        if possible == end:
            paths.append((start, end))
        recursive = find_all_paths_part2(graph, possible, end, seen.copy())
        paths.extend((start,) + path for path in recursive)
    return paths

def part1(puzzle) -> int:
    graph = parse_lines(puzzle)
    return len(find_all_paths_part1(graph, 'start', 'end', seen={'start'}))

def part2(puzzle) -> int:
    graph = parse_lines(puzzle)
    return len(find_all_paths_part2(graph, 'start', 'end', seen=defaultdict(int)))

print(part1(puzzle_input))
print(part2(puzzle_input))
