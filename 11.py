from typing import List, Dict
from collections import defaultdict


def preprocess() -> List[str]:
    with open("input/11.txt") as f:
        data = f.read().strip("\n").split()
    return data


def blink(data: Dict[int, int]) -> Dict[int, int]:
    new = defaultdict(int)
    for i in data:
        if i == "0":
            new["1"] += data[i]
        elif len(i) % 2 == 0:
            new[str(int(str(i)[: len(str(i)) // 2]))] += data[i]
            new[str(int(str(i)[len(str(i)) // 2 :]))] += data[i]
        else:
            new[str(int(i) * 2024)] += data[i]
        data[i] = 0
    return new


def partA(content: List[str]):
    data: Dict[int, int] = {}
    for i in content:
        if i not in data:
            data[i] = 0
        data[i] += 1
    for _ in range(25):
        data = blink(data)
    print(sum(data.values()))


def partB(content: List[str]):
    data: Dict[int, int] = {}
    for i in content:
        if i not in data:
            data[i] = 0
        data[i] += 1
    for _ in range(75):
        data = blink(data)
    print(sum(data.values()))


if __name__ == "__main__":
    data = preprocess()
    partA(data)
    partB(data)
