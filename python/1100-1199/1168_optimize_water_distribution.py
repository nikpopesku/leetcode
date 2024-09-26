from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        self.root = []
        self.rank = []

    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        pipes.sort(key=lambda x: x[-1])
        totalCost = 0
        self.root = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

        for a, b, c in pipes:
            if self.find(a - 1) == self.find(b - 1):
                continue

            totalCost += c
            self.union(a - 1, b - 1)

        totalCost += sum(
            [min([wells[k] for k in range(len(self.root)) if self.root[k] == nw]) for nw in set(self.root)])

        return totalCost

    def union(self, a: int, b: int):
        rootA, rootB = self.find(a), self.find(b)

        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.root[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.root[rootA] = rootB
            else:
                self.root[rootA] = rootB
                self.rank[rootB] += 1

    def find(self, a: int):
        if a == self.root[a]:
            return a

        self.root[a] = self.find(self.root[a])

        return self.root[a]

solution = Solution()
print(solution.minCostToSupplyWater(n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]))