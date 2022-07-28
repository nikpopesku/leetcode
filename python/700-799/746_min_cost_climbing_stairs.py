import sys
from typing import List, Set


class Solution:
    def __init__(self):
        self.hashmap = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) in [1, 2]:
            return min(cost)

        if len(cost) not in self.hashmap:
            self.hashmap[len(cost)] = min(cost[-1] + self.minCostClimbingStairs(cost[:-1]),
                                          cost[-2] + self.minCostClimbingStairs(cost[:-2]))

        return self.hashmap[len(cost)]


solution = Solution()
print(solution.minCostClimbingStairs(cost = [10,15,20]))