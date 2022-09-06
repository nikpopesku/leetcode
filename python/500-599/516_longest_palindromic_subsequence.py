import sys
from typing import List


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        def rec(l, r):
            if (l, r) in dp:
                return dp[(l, r)]

            if l > r:
                return 0
            if l == r:
                return 1

            dp[(l, r)] = 2 + rec(l + 1, r - 1) if s[l] == s[r] else max(rec(l + 1, r), rec(l, r - 1))

            return dp[(l, r)]

        return rec(0, len(s) - 1)


solution = Solution()
print(solution.longestPalindromeSubseq(s = "aabaa"))