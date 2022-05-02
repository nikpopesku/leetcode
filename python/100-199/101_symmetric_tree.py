from typing import Optional, List
from treenode import TreeNode

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return True


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.isSymmetric(root = root))