from typing import List
from math import atan

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        proportion0 = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        for i in range(2, len(coordinates)):
            if proportion0 != (coordinates[i][1] - coordinates[1][1]) / (coordinates[i][0] - coordinates[1][0]):
                return False
        else:
            return True





solution = Solution()
print(solution.checkStraightLine(coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))