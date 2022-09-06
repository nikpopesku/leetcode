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

            if s[l] == s[r]:
                return 2 + rec(l + 1, r - 1)
            else:
                return max(rec(l + 1, r), rec(l, r - 1))

        return rec(0, len(s) - 1)


solution = Solution()
print(solution.longestPalindromeSubseq(s = "aabaa"))