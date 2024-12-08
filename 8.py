from itertools import permutations
from collections import defaultdict
from typing import Tuple, DefaultDict, List


def preprocess() -> Tuple[Tuple[int, int], DefaultDict[int, List]]:
    data = defaultdict(list)
    with open("input/8.txt") as f:
        for y, line in enumerate(f.read().splitlines()):
            for x, val in enumerate(line.rstrip("\n")):
                if val not in [".", "#"]:
                    data[val].append((x, y))

    return (x, y), data


def partA(content: Tuple[Tuple[int, int], DefaultDict[int, List]]):
    (x, y), data = content
    anti_nodes_total = set()
    for _, locations in data.items():
        for p in permutations(locations, 2):
            j = 1
            while True:
                anti = (
                    p[0][0] + (p[0][0] - p[1][0]) * j,
                    p[0][1] + (p[0][1] - p[1][1]) * j,
                )
                if anti[0] >= 0 and anti[0] <= x and anti[1] >= 0 and anti[1] <= y:
                    if j == 1:
                        anti_nodes_total.add(anti)
                    j += 1
                else:
                    break
    print(len(anti_nodes_total))


def partB(content: Tuple[Tuple[int, int], DefaultDict[int, List]]):
    (x, y), data = content
    anti_nodes_total2 = set()
    for _, locations in data.items():
        for p in permutations(locations, 2):
            j = 1
            anti_nodes_total2.add(p[0])
            while True:
                anti = (
                    p[0][0] + (p[0][0] - p[1][0]) * j,
                    p[0][1] + (p[0][1] - p[1][1]) * j,
                )
                if anti[0] >= 0 and anti[0] <= x and anti[1] >= 0 and anti[1] <= y:
                    anti_nodes_total2.add(anti)
                    j += 1
                else:
                    break
    print(len(anti_nodes_total2))


if __name__ == "__main__":
    data = preprocess()
    partA(data)
    partB(data)
