import sys
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers = list(range(1, n+1))
        response = []

        def combine_recurrent(numbers: List, response: List, temp_solution: List, k: int):
            while numbers and k > 0:
                temp_solution = numbers.pop()
                k -= 1

                return combine_recurrent(numbers, response, temp_solution, k)

            response.append(temp_solution)

            return response

        return combine_recurrent(numbers, response, [], k)





solution = Solution()
print(solution.combine(n = 4, k = 2))