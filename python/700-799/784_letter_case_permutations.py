import sys
from typing import List, Set

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def permute_all(i):
            if i == len(s) - 1:
                result.append(s)

            for j in range(i, len(s)):
                temp = s[:i] if i > 0 else '' + s[i].upper() + s[i+1:] if i+1 < len(s) else ''
                s[i].upper() if temp.upper() == s[i] else temp.lower()
                permute_all(i+1)
                s[j], s[i] = s[i], s[j]
                j += 1

        result = []
        permute_all(0)
        return result





solution = Solution()
print(solution.letterCasePermutation(s = "a1b2"))