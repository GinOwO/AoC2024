from typing import List
from math import prod
import re

P = re.compile(r"p=([\-\+]?\d+),([\-\+]?\d+) v=([\-\+]?\d+),([\-\+]?\d+)")


def preprocess() -> List[List[int]]:
    with open("input/14.txt") as f:
        data = P.findall(f.read())
    return [[int(i) for i in v] for v in data]


def partA(data: List[List[int]]):
    dimen = (101, 103)
    quadrants = [[0, 0], [0, 0]]
    for x, y, vx, vy in data:
        sx, sy = (
            (dimen[0] + x + (vx * 100) % dimen[0]) % dimen[0],
            (dimen[1] + y + (vy * 100) % dimen[1]) % dimen[1],
        )
        if sx == dimen[0] // 2 or sy == dimen[1] // 2:
            continue
        quadrants[sy > dimen[1] // 2][sx > dimen[0] // 2] += 1
    print(prod(prod(i) for i in quadrants))


def partB(data: List[List[int]]):
    dimen = (101, 103)
    for second in range(1, dimen[0] * dimen[1] + 1):
        data = [
            ((px + vx) % dimen[0], (py + vy) % dimen[1], vx, vy)
            for px, py, vx, vy in data
        ]
        if len({(px, py) for px, py, _2, _3 in data}) == len(data):
            print(second)
            return


if __name__ == "__main__":
    data = preprocess()
    partA(data)
    partB(data)
