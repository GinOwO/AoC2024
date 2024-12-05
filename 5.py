from collections import defaultdict
from typing import List, DefaultDict, Tuple, Set, Dict


def preprocess() -> Tuple[Dict[int, List[int]], List[List[int]]]:
    graph = defaultdict(list)
    orderings = []
    topos = {}
    index = 0
    with open("input/5.txt") as f:
        while (line := f.readline()) != "\n":
            a, b = [int(i) for i in line.split("|")]
            graph[a].append(b)

        while line := f.readline():
            orderings.append([int(i) for i in line.split(",")])
            topos[index] = toposort(graph, set(orderings[-1]))
            index += 1
    return (topos, orderings)


def toposort(adj_list: DefaultDict[int, List[int]], vertices: Set[int]) -> List[int]:
    in_degree = defaultdict(int)
    for u in vertices:
        for v in adj_list[u]:
            if v in vertices:
                in_degree[v] += 1

    queue = [v for v in vertices if in_degree[v] == 0]
    topo_order = []

    while queue:
        current = queue.pop(0)
        topo_order.append(current)
        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) == len(vertices):
        return topo_order
    raise Exception("Topo Failed")


def is_valid_subseq(seq: List[int], subseq: List[int]):
    i, j = 0, 0
    while i < len(subseq) and j < len(seq):
        if seq[j] == subseq[i]:
            i += 1
        j += 1
    return i == len(subseq)


def partA(topos: Dict[int, List[int]], orderings: List[List[int]]) -> List[int]:
    res = 0
    invalid = []
    for i, order in enumerate(orderings):
        if is_valid_subseq(topos[i], order):
            res += order[len(order) // 2]
        else:
            invalid.append(i)
    print(res)
    return invalid


def partB(orderings: List[List[int]], topos: Dict[int, List[int]], invalid: List[int]):
    res = 0
    for i in invalid:
        indices = {k: j for j, k in enumerate(topos[i])}
        res += sorted(orderings[i], key=indices.get)[len(orderings[i]) // 2]
    print(res)


if __name__ == "__main__":
    topos, ordering = preprocess()
    invalid = partA(topos, ordering)
    partB(ordering, topos, invalid)
