import sys
from typing import List, Set

class Solution:
    def reverseBits(self, n: int) -> int:
        response = 0
        i = 31
        while i:
            i -= 1
            response = (response + (n & 1)) << 1
            n = n >> 1

        return response


solution = Solution()
print(bin(solution.reverseBits(n = 3221225471)))