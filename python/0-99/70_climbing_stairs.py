import sys
from typing import List, Set

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers = list(range(1, n+1))
        response = []

        def combine_recurrent(numbers: List, response: List, temp_solution: Set, places: int):
            while numbers and places > 0:
                temp_solution.add(numbers.pop())
                places -= 1

                return combine_recurrent(numbers, response, temp_solution, places)

            if temp_solution not in response:
                response.append(temp_solution.copy())

            if numbers:
                temp_solution.pop()
                places += 1
                return combine_recurrent(numbers, response, temp_solution, places)

            return response

        return [list(i) for i in combine_recurrent(numbers, response, set(), k)]





solution = Solution()
print(solution.combine(n = 4, k = 2))