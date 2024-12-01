from typing import Dict, Tuple


def preprocess() -> Dict[Tuple[int, int], str]:
    data = {
        (i, j): c
        for i, s in enumerate(open("input/4.txt", "r").readlines())
        for j, c in enumerate(s)
    }

    return data


"""

   (1, 1)
"""

dirs = [-1, -1, 0, 0, 1, 1, 0, -1, 1, -1]


def partA(data: Dict[Tuple[int, int], str]):
    res = 0
    for i, j in data:
        for d in range(len(dirs) - 1):
            candidate = "".join(
                data.get((i + dirs[d] * k, j + dirs[d + 1] * k), "")
                for k in range(len("XMAS"))
            )
            res += candidate == "XMAS"

    print(res)


def partB(data: Dict[Tuple[int, int], str]):
    res = 0
    for i, j in data:
        if data[i, j] == "A":
            lr = data.get((i - 1, j - 1), "") + data.get((i + 1, j + 1), "")
            rl = data.get((i - 1, j + 1), "") + data.get((i + 1, j - 1), "")
            res += {lr, rl} <= {"MS", "SM"}

    print(res)


if __name__ == "__main__":
    data = preprocess()
    partA(data)
    partB(data)
