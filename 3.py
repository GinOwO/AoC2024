import re
from typing import Pattern


def preprocess() -> str:
    data = open("input/3.txt", "r").read()
    return data


P1 = re.compile(r"mul\((\d+),(\d+)\)")
P2 = re.compile(r"(?s)(?:(?<=don't\(\)).*?(?=do\(\)|$))|(?:mul\((\d+),(\d+)\))")


def solve(data: str, pattern: Pattern):
    muls = pattern.findall(data)
    res = 0
    for i, j in muls:
        res += int(i or 0) * int(j or 0)
    print(res)


if __name__ == "__main__":
    data = preprocess()
    solve(data, P1)
    solve(data, P2)
