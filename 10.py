from typing import List, Tuple, Set
from helperlib.constants import DIRS4


def preprocess() -> List[List[int]]:
    with open("input/10.txt", "r") as f:
        data = f.readlines()
    return [[int(i) for i in v.strip("\n")] for v in data]


def partA(map: List[List[int]]):
    reachable: List[List[Set[Tuple[int, int]]]] = [
        [-1 for j in range(len(map[i]))] for i in range(len(map))
    ]

    def walk(x: int, y: int) -> Set[Tuple[int, int]]:
        if map[x][y] == 9:
            a = set()
            a.add((x, y))
            return a

        if reachable[x][y] != -1:
            return reachable[x][y]

        reachable[x][y] = set()
        for i in range(4):
            a, b = x + DIRS4[i], y + DIRS4[i + 1]
            if (
                a >= 0
                and b >= 0
                and a < len(map)
                and b < len(map[0])
                and map[a][b] == map[x][y] + 1
            ):
                reachable[x][y] |= walk(a, b)

        return reachable[x][y]

    ans = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                ans += len(walk(i, j))
    print(ans)


def partB(map: List[List[int]]):
    ratings: List[List[int]] = [[-1] * len(map[0]) for _ in range(len(map))]

    def walk(x: int, y: int):
        if map[x][y] == 9:
            return True

        if ratings[x][y] != -1:
            return ratings[x][y]

        ratings[x][y] = 0
        for i in range(4):
            a, b = x + DIRS4[i], y + DIRS4[i + 1]
            if (
                a >= 0
                and b >= 0
                and a < len(map)
                and b < len(map[0])
                and map[a][b] == map[x][y] + 1
            ):
                ratings[x][y] += walk(a, b)

        return ratings[x][y]

    ans = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                ans += walk(i, j)
    print(ans)


if __name__ == "__main__":
    data = preprocess()
    partA(data)
    partB(data)
