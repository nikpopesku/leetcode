import sys
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        l,k = 0, len(matrix) - 1

        while l < k:
            submatrix = matrix[0:k]

            for i in range(len(submatrix) - 1):
                submatrix[i][len(submatrix) - 1], temp = submatrix[0][i], submatrix[i][len(submatrix) - 1]
                submatrix[len(submatrix) - 1][len(submatrix) - i - 1], temp = temp, submatrix[len(submatrix) - 1][len(submatrix) - i - 1]
                submatrix[len(submatrix) - i - 1][0], temp = temp, submatrix[len(submatrix) - i - 1][0]
                submatrix[0][i] = temp

            l = l + 1
            k = k - 1



solution = Solution()
print(solution.rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]]))