from typing import List
from functools import reduce


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        return [[sum(mat[i+k0][j+k1] for k0 in range(-k, k+1) for k1 in range(-k, k+1) if 0 <= i + k0 <= len(mat) - 1 and 0 <= j + k1 <= len(mat) - 1) for j in range(len(mat))] for i in range(len(mat))]

solution = Solution()
print(solution.matrixBlockSum(mat = [[67,64,78],[99,98,38],[82,46,46],[6,52,55],[55,99,45]], k = 3))