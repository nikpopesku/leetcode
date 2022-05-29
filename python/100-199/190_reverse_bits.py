import sys
from typing import List, Set

class Solution:
    def reverseBits(self, n: int) -> int:
        response = 0
        while n:
            temp = n & 1
            n = n >> 1
            response = (response << 1) + temp

        return n


solution = Solution()
print(solution.reverseBits(n = 10))