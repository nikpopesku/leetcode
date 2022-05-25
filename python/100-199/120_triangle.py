import sys
from typing import List, Set

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        nodes = {}
        length = len(triangle)
        last_element = None

        if length == 1:
            return triangle[0][0]

        nodes[0] = triangle[0][0]
        if length >= 2:
            nodes[1] = triangle[1][1] if triangle[1][0] > triangle[1][1] else triangle[1][0]
            last_element = 1 if triangle[1][0] > triangle[1][1] else 0

        for i in range(2, length):
            nodes[i] = min(triangle[i][last_element], triangle[i][last_element+1])
            last_element = last_element if triangle[i][last_element] < triangle[i][last_element+1] else last_element + 1

        return sum(nodes.values())




solution = Solution()
print(solution.minimumTotal(triangle = [[1],[2,3]]))