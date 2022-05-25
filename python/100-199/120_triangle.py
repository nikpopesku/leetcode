import sys
from typing import List, Set

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        nodes = {}
        length = len(triangle)

        if length == 1:
            return triangle[0][0]

        if length == 2:
            return triangle[1][0] if triangle[1][0] > triangle[1][1] else triangle[1][1]

        houses[1] = nums[0]
        houses[2] = nums[0] if nums[0] > nums[1] else nums[1]

        for i in range(3, length+1):
            houses[i] = max(houses[i-2] + nums[i-1], houses[i-1])

        return houses[length]




solution = Solution()
print(solution.minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))