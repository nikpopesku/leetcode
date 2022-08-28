from typing import Optional, List
from treenode import TreeNode

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [(1,), (1, 1), (1, 2, 1)]

        if rowIndex <= len(dp) - 1:
            return list(dp[rowIndex])

        for i in range(3, rowIndex + 1):
            dp.append(tuple(1 if j == 0 or j == len(dp[i - 1]) else dp[i - 1][j - 1] + dp[i - 1][j] for j in range(i + 1)))

        return list(dp[-1])


solution = Solution()
print(solution.getRow(rowIndex = 3))