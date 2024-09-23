from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        self.rank = []
        self.root = []

    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x: x[-1])
        totalCost = 0
        totalConnections = 0
        self.rank = [1 for i in range(n)]
        self.root = [i for i in range(n)]

        for a, b, cost in connections:
            if (self.root[a-1] == self.root[b-1]):
                continue
            totalCost += cost
            self.union(a-1, b-1)
            totalConnections += 1

        return totalCost if n - 1 == totalConnections else -1

    def union(self, a: int, b: int):
        rootA = self.root[a]
        rootB = self.root[b]

        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.root[rootB] = rootA
                self.rank[rootA] += 1
            else:
                self.root[rootA] = rootB
                self.rank[rootB] += 1

    def find(self, a: int):
        while a != self.root[a]:
            self.root[a] = self.root[self.root[a]]

            a = self.root[a]

        return a


solution = Solution()
print(solution.minimumCost(n = 4, connections = [[1,2,1],[1,3,2],[3,4,4],[1,4,3]]))