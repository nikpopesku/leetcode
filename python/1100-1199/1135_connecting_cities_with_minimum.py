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
        self.rank = [1 for i in range(1, n + 1)]
        self.root = [i for i in range(1, n + 1)]

        for a, b, cost in connections:
            if (self.root[a] == self.root[b]):
                continue
            totalCost += cost
            self.union(a, b)
            totalConnections += 1

        return totalCost if len(connections) - 1 == totalConnections else -1

        return totalCost

    def union(a: int, b: int):
        rootA = self.root[a]
        rootB = self.root[b]

        if rootA != rootB:
            if self.rank[a] > self.rank[b]:
                self.root[rootB] = rootA
                self.rank[a] += 1
            else:
                self.root[rootA] = rootB
                self.rank[b] += 1

    def find(a: int):
        while a != self.root[a]:
            self.root[a] = self.root[self.root[a]]

            a = self.root[a]

        return a


solution = Solution()
print(solution.minimumCost(n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]))