import re


def preprocess() -> str:
    data = open("input/3.txt", "r").read()
    return data


P1 = re.compile(r"mul\((\d+),(\d+)\)")
P2 = re.compile(r"(?:(do|don\'t)\(\)|mul\((\d+),(\d+)\))")


def partA(data: str):
    muls = P1.findall(data)
    res = 0
    for i, j in muls:
        res += int(i) * int(j)
    print(res)


def partB(data):
    muls = P2.findall("do()" + data)
    res = 0
    do = True
    for X in muls:
        if X[0] == "do":
            do = True
        elif X[0] == "don't":
            do = False
        elif do:
            res += int(X[1]) * int(X[2])
    print(res)


if __name__ == "__main__":
    data = preprocess()
    partA(data)
    partB(data)
