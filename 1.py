from typing import Tuple, List
from collections import Counter


def preprocess():
    with open("input/1.txt", "r") as f:
        data = f.readlines()
    a, b = [], []
    for i in data:
        p = i.split()
        a.append(int(p[0]))
        b.append(int(p[1]))
    a.sort()
    b.sort()
    return a, b


def partA(data: Tuple[List, List]):
    a, b = data
    print(sum(abs(i - j) for i, j in zip(a, b)))
    return a, b


def partB(data: Tuple[List, List]):
    a, b = data
    cnt = Counter(b)
    print(sum(i * cnt[i] for i in a))


if __name__ == "__main__":
    data = preprocess()
    partA(data)
    partB(data)
