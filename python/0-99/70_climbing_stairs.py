import sys
from typing import List, Set

class Solution:
    values = {
        1: 1,
        2: 2,
        3: 3
    }
    def climbStairs(self, n: int) -> int:
        if n in self.values:
            return self.values[n]

        self.values[n-2] = self.climbStairs(n-2)
        self.values[n-1] = self.climbStairs(n-1)
        self.values[n] = self.climbStairs(n-2) + self.climbStairs(n-1)

        return self.climbStairs(n)




solution = Solution()
print(solution.climbStairs(n = 10))