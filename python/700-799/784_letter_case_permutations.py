import sys
from typing import List, Set

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def permute_all(i, current_string):
            if i == len(s) - 1:
                result.append(current_string)

            for j in range(i, len(s)):
                temp = (current_string[:j] if j > 0 else '') + current_string[j].upper() + (current_string[j+1:] if j+1 < len(s) else '')
                permute_all(i+1, temp)
                permute_all(i+1, current_string)

        result = []
        permute_all(0, s)
        return result





solution = Solution()
print(solution.letterCasePermutation(s = "a1b2"))