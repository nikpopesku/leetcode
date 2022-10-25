from typing import List


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        array_s = list(s)

        for lenght in range(1, (len(s) // 2) + 1):
            if len(s) % lenght == 1:
                continue
            if array_s[:lenght] * int(len(s) // lenght) == array_s:
                return True

        return False


solution = Solution()
print(solution.repeatedSubstringPattern(s = "abab"))