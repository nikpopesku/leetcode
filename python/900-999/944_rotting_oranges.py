import sys
from typing import List, Dict


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        matrix = [[float('inf')] * cols] * rows

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue
                elif grid[i][j] == 2:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = min(matrix[i][j], min(matrix[i-1][j] if i-1 >= 0 else matrix[i][j], matrix[i][j-1] if j - 1 >= 0 else matrix[i][j]) + 1)

        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                if grid[i][j] == 0 or grid[i][j] == 2:
                    continue
                else:
                    matrix[i][j] = min(matrix[i][j], min(matrix[i+1][j] if i+1 < rows else matrix[i][j], matrix[i][j+1] if j+1 < cols else matrix[i][j]) + 1)

        return -1




solution = Solution()
print(solution.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))