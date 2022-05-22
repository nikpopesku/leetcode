import sys
from typing import List, Set

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers = list(range(1, n+1))
        response = set()

        def combine_recurrent(numbers: List, response: Set, temp_solution: Set, k: int):
            while numbers and k > 0:
                temp_solution.add(numbers.pop())
                k -= 1

                return combine_recurrent(numbers, response, temp_solution, k)

            if temp_solution not in response:
                response.add(temp_solution)
            else:
                temp_solution.pop()
                k += 1
                return combine_recurrent(numbers, response, temp_solution, k)

            return response

        return list(combine_recurrent(numbers, response, set(), k))





solution = Solution()
print(solution.combine(n = 4, k = 2))