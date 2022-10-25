from typing import Optional, List
from treenode import TreeNode

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.isBalanced(root.left) if root.left else True) and (self.isBalanced(root.right) if root.right else True) and \
               abs((Solution.getHeight(root.left) if root.left else 0) - (Solution.getHeight(root.right) if root.right else 0)) <= 1

    @staticmethod
    def getHeight(root: Optional[TreeNode]) -> int:
        return 1 + max(Solution.getHeight(root.left) if root.left else 0,
                       Solution.getHeight(root.right) if root.right else 0)


r1 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
solution = Solution()
print(solution.isBalanced(root = r1))