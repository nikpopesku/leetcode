from typing import List
from functools import reduce

class Solution:
    def __init__(self):
        self.hashmap = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        if n not in self.hashmap:
            self.hashmap[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

        return self.hashmap[n]

solution = Solution()
print(solution.tribonacci(n = 0))