import sys
from typing import List, Dict


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        matrix = [[float('inf') for col in range(cols)] for row in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    matrix[i][j] = None
                elif grid[i][j] == 2:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = min(
                        matrix[i][j],
                        min(
                            matrix[i-1][j] if i-1 >= 0 and matrix[i-1][j] is not None else matrix[i][j],
                            matrix[i][j-1] if j - 1 >= 0 and matrix[i][j-1] is not None else matrix[i][j]
                        ) + 1
                    )

        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                if grid[i][j] == 0 or grid[i][j] == 2:
                    continue
                else:
                    matrix[i][j] = min(
                        matrix[i][j],
                        min(
                            matrix[i+1][j] if i+1 < rows and matrix[i+1][j] is not None else matrix[i][j],
                            matrix[i][j+1] if j+1 < cols and matrix[i][j+1] is not None else matrix[i][j]
                        ) + 1
                    )

        max_time = -1

        for i in range(rows):
            for j in range(cols):
                max_time = max(max_time, matrix[i][j] if matrix[i][j] != None else max_time)


        return max_time if max_time != float('inf') else -1



solution = Solution()
print(solution.orangesRotting(grid = [[0,2]]))