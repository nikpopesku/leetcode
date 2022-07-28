import sys
from typing import List, Set


class Solution:
    def __init__(self):
        self.hashmap = {0: 0}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            self.hashmap[1] = cost[0]
            return cost[0]

        if len(cost) not in self.hashmap:
            self.hashmap[len(cost)] = min(cost[-1] + self.minCostClimbingStairs(cost[:-1]), cost[-2] + self.minCostClimbingStairs(cost[:-2]))

        return self.hashmap[len(cost)]


solution = Solution()
print(solution.minCostClimbingStairs(cost = [10,15,20]))
xx = 5