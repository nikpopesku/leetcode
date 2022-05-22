import sys
from typing import List, Set

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def permute_all(i, current_string):
            if i == len(s):
                result.add(current_string)

            for j in range(i, len(s)):
                if current_string[j].lower() >= 'a' and current_string[j].lower() <= 'z':
                    changed_string = (current_string[:j] if j > 0 else '') + \
                                     (current_string[j].upper() if current_string[j].lower() == current_string[j] else current_string[j].lower()) + \
                                     (current_string[j+1:] if j+1 < len(s) else '')
                    permute_all(i+1, changed_string)
                permute_all(i+1, current_string)

        result = set()
        permute_all(0, s)
        return list(result)





solution = Solution()
print(len(solution.letterCasePermutation(s = "qMKfHUf")))