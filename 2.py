from typing import List


def preprocess():
    with open("input/2.txt", "r") as f:
        data = f.readlines()
    arr = []
    for i in data:
        arr.append([int(i) for i in i.split()])
    return arr


def signum(n: int):
    return n / abs(n or 1)


def checkA(row: List[int]) -> bool:
    return all(
        signum(row[i] - row[i - 1]) == signum(row[i + 1] - row[i])
        and 1 <= abs(row[i] - row[i - 1]) <= 3
        and 1 <= abs(row[i + 1] - row[i]) <= 3
        for i in range(1, len(row) - 1)
    )


def checkB(row: List[int]) -> bool:
    if checkA(row):
        return True
    for i in range(len(row)):
        if checkA(row[:i] + row[i + 1 :]):
            return True
    return False


def partA(data: List[List[int]]):
    print(sum(checkA(i) for i in data))


def partB(data: List[List[int]]):
    print(sum(checkB(i) for i in data))


if __name__ == "__main__":
    data = preprocess()
    partA(data)
    partB(data)
