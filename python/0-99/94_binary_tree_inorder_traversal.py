from typing import Optional, List
from treenode import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        response = []

        if root and root.left:
            response += self.inorderTraversal(root.left)

        if root:
            response += [root.val]

        if root and root.right:
            response += self.inorderTraversal(root.right)

        return response

r1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
solution = Solution()
print(solution.inorderTraversal(root = r1))