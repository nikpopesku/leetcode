from typing import List
from functools import reduce


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:


solution = Solution()
print(solution.nearestValidPoint(x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]))