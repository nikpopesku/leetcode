from typing import Optional, List
from treenode import TreeNode

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return -1 <= (Solution.getHeight(root.left) if root.left else 0) - (
            Solution.getHeight(root.right) if root.right else 0) <= 1

    @classmethod
    def getHeight(root: Optional[TreeNode]) -> int:
        return 1 + max(Solution.getHeight(root.left) if root.left else 0,
                       Solution.getHeight(root.right) if root.right else 0)


solution = Solution()
print(solution.isBalanced(root = [1,2,2,3,3,null,null,4,4]))