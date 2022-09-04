import sys
from typing import List, Set

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [int(matrix[0][j]) for j in range(len(matrix[0]))]
        max_dp = float('-inf')

        for i in range(1, len(matrix)):
            element = [int(matrix[i][0])]
            for j in range(1, len(matrix[i])):
                if (matrix[i - 1][j - 1] == '1'):
                    current = int(matrix[i][j])
                    element.append(min(dp[i - 1][j - 1], dp[i - 1][j], element[-1]) + current)
                else:
                    element.append(int(matrix[i][j]))

            dp = element
            max_dp = max(*dp, max_dp)

        return int(max_dp * max_dp)


solution = Solution()
print(solution.maximalSquare(matrix = [["0","1"],["1","0"]]))