import sys
from typing import List, Set

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def permute_all(i, current_string: List[str]):
            if i == len_s:
                result.add(current_string)

            for j in range(i, len_s):
                lower = current_string[j].lower()
                if 'a' <= lower <= 'z':
                    changed_string = (current_string[:j] if j > 0 else '') + \
                                     (current_string[j].upper() if lower == current_string[j] else lower) + \
                                     (current_string[j+1:] if j+1 < len_s else '')
                    permute_all(i+1, changed_string)
                permute_all(i+1, current_string)

        result = set()
        len_s = len(s)
        permute_all(0, list(s))
        return list(result)





solution = Solution()
print(len(solution.letterCasePermutation(s = "k5qo0LdW")))