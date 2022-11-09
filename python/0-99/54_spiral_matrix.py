import sys
from typing import List, Set

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height_l, height_k = 0, len(matrix)
        width_l, width_k = 0, len(matrix[0])

        response = []

        while width_l < width_k and height_l < height_k:
            response = response + matrix[height_l][width_l:width_k]
            response = response + [matrix[i][width_k - 1] for i in range(height_l+1, height_k - 1)]
            response = response + matrix[height_k - 1][width_l:width_k:-1]
            response = response + [matrix[i][width_l] for i in range(height_k-1, height_l - 1, -1)]
            width_l = width_l + 1
            width_k = width_k - 1
            height_l = height_l + 1
            height_k = height_k - 1

        return response



solution = Solution()
print(solution.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))