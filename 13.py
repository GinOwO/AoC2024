from typing import List
import re

P = re.compile(
    r"Button A: X([\-\+]?\d+), Y.([\-\+]?\d+)\nButton B: X.([\-\+]?\d+), Y.([\-\+]?\d+)\nPrize: X=([\-\+]?\d+), Y=([\-\+]?\d+)"
)


def preprocess() -> List[List[int]]:
    with open("input/13.txt") as f:
        data = P.findall(f.read())
    return [[int(i) for i in v] for v in data]


fX = lambda a1, a2, b1, b2, c1, c2: (b2 * c1 - b1 * c2) / (b2 * a1 - b1 * a2)
fY = lambda a, b, c, x: (c - a * x) / b


def partA(data: List[List[int]]):
    ans = 0
    for i in data:
        try:
            X = fX(*i)
            if X != int(X):
                continue
            Y = fY(i[0], i[2], i[4], X)
            if Y != int(Y):
                continue
            if X <= 100 and Y <= 100:
                ans += X * 3 + Y
        except:
            pass
    print(ans)


def partB(data: List[List[int]]):
    ans = 0
    for i in data:
        i[4] += 1e13
        i[5] += 1e13
        try:
            X = fX(*i)
            if X != int(X):
                continue
            Y = fY(i[0], i[2], i[4], X)
            if Y != int(Y):
                continue
            ans += X * 3 + Y
        except:
            pass
    print(ans)


if __name__ == "__main__":
    data = preprocess()
    partA(data)
    partB(data)
