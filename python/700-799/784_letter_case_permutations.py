import sys
from typing import List, Set

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def permute_all(i, current_string: List[str]):
            if i == len_s:
                result.append(current_string)

            for j in range(i, len_s):
                lower = current_string[j].lower()
                permute_all(i+1, current_string)
                if 'a' <= lower <= 'z':
                    current_string[j] = current_string[j].upper() if lower == current_string[j] else lower
                    permute_all(i+1, current_string)

        result = []
        len_s = len(s)
        permute_all(0, list(s))
        return list(result)





solution = Solution()
print(len(solution.letterCasePermutation(s = "k5qo0LdW")))