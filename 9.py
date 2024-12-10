from typing import List
from copy import deepcopy


def preprocess() -> List[int]:
    with open("input/9.txt", "r") as f:
        data = f.read().strip("\n")
    arr = []
    flag = True
    num = -1
    for i in data:
        arr.extend([-1 if (flag := not flag) else (num := num + 1)] * int(i))
    return arr


def partA(data: List[int]):
    arr = deepcopy(data)
    left, right = 0, len(arr) - 1
    while left < right:
        while left < right and arr[left] != -1:
            left += 1
        while left < right and arr[right] == -1:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    print(sum(max(0, n) * i for i, n in enumerate(arr)))


def find(begin: int, end: int, size: int, arr: List[int]):
    cz = 0
    if size == 1:
        idx = arr.index(-1)
        if idx > end:
            return -1
        return idx
    for i in range(begin, end):
        cz = (cz * (arr[i] == -1 and i > 0 and arr[i] == arr[i - 1])) + 1
        if cz >= size:
            return i - size + 1
    return -1


def skip_rl(rbegin: int, num: int, arr: List[int]):
    while rbegin >= 0:
        if arr[rbegin] != num:
            return rbegin
        rbegin -= 1
    return -1


def vis(arr):
    return f"{''.join(str(i) if i != -1 else '.' for i in arr)}"


def partB(data: List[int]):
    arr = deepcopy(data)
    seen = set()
    right = len(arr) - 1
    while right >= 0:
        while right >= 0 and arr[right] == -1:
            right -= 1

        if right >= 0:
            rend = skip_rl(right, arr[right], arr)
            pos = find(0, rend, right - rend, arr)
            if pos == -1 or arr[right] in seen:
                right = rend
                continue
            seen.add(arr[right])
            for _ in range(right - rend):
                arr[pos], arr[right] = arr[right], arr[pos]
                pos += 1
                right -= 1
    print(sum(max(0, n) * i for i, n in enumerate(arr)))


if __name__ == "__main__":
    data = preprocess()
    partA(data)
    partB(data)
