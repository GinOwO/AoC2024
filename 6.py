from typing import List


def preprocess() -> List[str]:
    with open("input/6.txt", "r") as f:
        data = f.readlines()
    return [list(i.strip("\n")) for i in data]


dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))


def check(x: int, y: int, dir: int, data: List[str], visited: List[List[int]]):
    while not (visited[x][y] & (1 << dir)):
        visited[x][y] |= 1 << dir

        a, b = x + dirs[dir][0], y + dirs[dir][1]
        if 0 <= a < len(data) and 0 <= b < len(data[0]):
            if data[a][b] == "#":
                dir = (dir + 1) % 4
            else:
                x, y = a, b
        else:
            return False
    return True


def partA(data: List[str]):
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] in "^>v<":
                break
        else:
            continue
        break

    visited = [[0] * len(data[0]) for _ in range(len(data))]
    check(x, y, "^>v<".index(data[x][y]), data, visited)

    print(sum(k != 0 for p in visited for k in p))


def partB(data: List[str]):
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] in "^>v<":
                break
        else:
            continue
        break

    res = 0
    dir = "^>v<".index(data[x][y])
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != "#":
                visited = [[0] * len(data[0]) for _ in range(len(data))]
                data[i][j] = "#"
                res += check(x, y, dir, data, visited)
                data[i][j] = "."

    print(res)


if __name__ == "__main__":
    data = preprocess()
    partA(data)
    partB(data)
