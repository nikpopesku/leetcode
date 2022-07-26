from typing import List
from functools import reduce


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return ''.join(set(t) - set(s))


solution = Solution()
print(solution.findTheDifference(s = "abcd", t = "abcde"))