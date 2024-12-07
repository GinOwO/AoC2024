from typing import List
from math import log10, floor


def preprocess() -> List[List[int]]:
    data = []
    with open("input/7.txt", "r") as f:
        while line := f.readline().strip().split():
            data.append([int(i.strip(":")) for i in line])
    return data


def partA(data: List[List[int]]):
    def check(i: int, current: int):  # SAT
        if i == len(args) or current > target:
            return target == current

        return check(i + 1, current + args[i]) or check(i + 1, current * args[i])

    res = 0
    for line in data:
        target, args = line[0], line[1:]

        if check(1, line[1]):
            res += line[0]
    print(res)


def partB(data: List[List[int]]):
    def check(i: int, current: int):
        # Early prune with c > t makes it faster by 1 second
        if i == len(args) or current > target:
            return target == current

        return (
            check(i + 1, current + args[i])
            or check(i + 1, current * args[i])
            # 500ms boost over int(str(a) + str(b))
            or check(i + 1, current * (10 ** (floor(log10(args[i])) + 1)) + args[i])
        )

    res = 0
    for line in data:
        target, args = line[0], line[1:]

        if check(1, line[1]):
            res += line[0]
    print(res)


if __name__ == "__main__":
    data = preprocess()
    partA(data)
    partB(data)

"""
> time py 7.py
12839601725877
149956401519484

real    0m1.953s
user    0m1.902s
sys     0m0.043s
"""
