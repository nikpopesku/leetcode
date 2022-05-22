import sys
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers = list(range(1, n+1))

        def xxx(numbers: List, response: List, k: int):
            while numbers and k > 0:
                response.append(numbers.pop())
                k -= 1

                return xxx(numbers, response, k)

            return response

        return xxx(numbers, [], k)





solution = Solution()
print(solution.combine(n = 4, k = 2))