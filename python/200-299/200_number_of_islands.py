import sys
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return 4

solution = Solution()
print(solution.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))