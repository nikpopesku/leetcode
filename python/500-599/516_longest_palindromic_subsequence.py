import sys
from typing import List


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        maxl = 1
        maxs = s[0]

        for i in range(len(s)):
            temp = None

            for j in range(i + maxl, len(s)):
                temp = s[i:j + 1] if temp is None else temp + s[j]

                if temp == temp[::-1]:
                    maxl += 1
                    maxs = temp
                else:
                    temp = temp[:len(temp) - 1]

        return maxl


solution = Solution()
print(solution.longestPalindromeSubseq(s = "bbbab"))