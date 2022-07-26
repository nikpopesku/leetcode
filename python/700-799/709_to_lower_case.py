from typing import List
from functools import reduce


class Solution:
    def toLowerCase(self, s: str) -> str:
        answer = []
        for i in range(len(s)):
            delta = 32 if 65 <= ord(s[i]) <= 90 else 0
            answer.append(ord(s[i]) + delta)

        return ''.join(answer)



solution = Solution()
print(solution.toLowerCase(s = "LOVELY"))