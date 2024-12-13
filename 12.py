from typing import List
from string import ascii_uppercase
from collections import defaultdict
from helperlib.constants import DIRS4


def preprocess() -> List[str]:
    with open("input/12.txt", "r") as f:
        data = f.readlines()
    return [i.strip("\n") for i in data]


def partA(data: List[str]):
    visited = [[0] * len(i) for i in data]
    color = defaultdict(list)

    def dfs(i: int, j: int, data: List[str]):
        visited[i][j] = True
        color[data[i][j]][-1][0] += 1
        pm = 0

        for k in (0, 1, 2, 3):
            x, y = i + DIRS4[k], j + DIRS4[k + 1]
            if (
                x >= 0
                and y >= 0
                and x < len(data)
                and y < len(data[x])
                and not visited[x][y]
                and data[i][j] == data[x][y]
            ):
                dfs(x, y, data)

            pm += (
                x >= 0
                and y >= 0
                and x < len(data)
                and y < len(data[x])
                and data[i][j] == data[x][y]
            )

        color[data[i][j]][-1][1] += 4 - pm

    for i in range(len(data)):
        for j in range(len(data[i])):
            if not visited[i][j]:
                color[data[i][j]].append([0, 0])
                dfs(i, j, data)

    ans = 0
    for i in ascii_uppercase:
        for j in range(len(color[i])):
            ans += color[i][j][0] * color[i][j][1]

    print(ans)


def partB(data: List[str]):
    visited = [[0] * len(i) for i in data]
    perimeter = [[None] * len(i) for i in data]
    color = defaultdict(list)

    def dfs(i: int, j: int, data: List[str], prev: int):
        visited[i][j] = True
        color[data[i][j]][-1][0] += 1
        pm = 0

        for k in (0, 1, 2, 3):
            x, y = i + DIRS4[k], j + DIRS4[k + 1]
            if (
                x >= 0
                and y >= 0
                and x < len(data)
                and y < len(data[x])
                and not visited[x][y]
                and data[i][j] == data[x][y]
            ):
                dfs(x, y, data)

            pm += (
                x >= 0
                and y >= 0
                and x < len(data)
                and y < len(data[x])
                and data[i][j] == data[x][y]
            )

        if pm != 4:
            perimeter[i][j] = prev

    for i in range(len(data)):
        for j in range(len(data[i])):
            if not visited[i][j]:
                color[data[i][j]].append([0, 0])
                dfs(i, j, data)

    ans = 0
    for i in ascii_uppercase:
        for j in range(len(color[i])):
            ans += color[i][j][0] * color[i][j][1]

    print(ans)


if __name__ == "__main__":
    data = preprocess()
    partA(data)
    partB(data)
