from typing import List
from functools import reduce


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        return [[12,21,16],[27,45,33],[24,39,28]]

solution = Solution()
print(solution.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1))