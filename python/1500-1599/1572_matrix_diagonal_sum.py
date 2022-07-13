from typing import List
from functools import reduce


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        return sum([mat[i][i] for i in range(len(mat))])

solution = Solution()
print(solution.diagonalSum(mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]))