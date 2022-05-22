import sys
from typing import List, Set

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def permute_all(i):
            if i == len(s) - 1:
                result.append(s)

            j = i
            while j < len(s):
                s[i], s[j] = s[j], s[i]
                permute_all(i+1)
                s[j], s[i] = s[i], s[j]
                j += 1

        result = []
        permute_all(0)
        return result





solution = Solution()
print(solution.letterCasePermutation(s = "a1b2"))