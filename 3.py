import re


def preprocess() -> str:
    data = open("input/3.txt", "r").read()
    return data


P1 = re.compile(r"mul\((\d+),(\d+)\)")
P2 = re.compile(r"(?s)(?:(?<=don't\(\)).*?(?=do\(\)|$))|(?:mul\((\d+),(\d+)\))")


def partA(data: str):
    muls = P1.findall(data)
    res = 0
    for i, j in muls:
        res += int(i) * int(j)
    print(res)


def partB(data: str):
    muls = P2.findall(data)
    res = 0
    for i, j in muls:
        if i and j:
            res += int(i) * int(j)
    print(res)


if __name__ == "__main__":
    data = preprocess()
    partA(data)
    partB(data)
