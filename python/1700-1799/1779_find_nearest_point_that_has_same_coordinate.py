from typing import List
from functools import reduce


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minimum = float('inf')
        minimum_position = -1
        for i in range(len(points)):
            if (points[i][0] == x or points[i][1] == y) and (abs(x - points[i][0]) + abs(x - points[i][0]) < minimum):
                minimum = abs(x - points[i][0]) + abs(x - points[i][0])
                minimum_position = i

        return minimum_position



solution = Solution()
print(solution.nearestValidPoint(x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]))