from typing import List
from functools import reduce


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash = {}
        for i in range(len(s)):
            hash[s[i]] = hash[s[i]] + 1 if s[i] in hash.keys() else 1
        for i in range(len(t)):
            if s[i] not in hash.keys() or hash[s[i]] == 0:
                return s[i]
            else:
                hash[s[i]] = hash[s[i]] - 1


solution = Solution()
print(solution.findTheDifference(s = "abcd", t = "abcde"))