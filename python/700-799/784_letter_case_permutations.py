import sys
from typing import List, Set

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def permute_all(index, current_string: List[str]):
            if index == len_s:
                result.add(str(current_string))

            for j in range(index, len_s):
                lower = current_string[j].lower()
                permute_all(j+1, current_string)
                if 'a' <= lower <= 'z':
                    current_string[j] = current_string[j].upper() if lower == current_string[j] else lower
                    permute_all(j+1, current_string)

        result = set()
        len_s = len(s)
        permute_all(0, list(s))
        return list(result)





solution = Solution()
print(len(solution.letterCasePermutation(s = "k5qo0LdW")))