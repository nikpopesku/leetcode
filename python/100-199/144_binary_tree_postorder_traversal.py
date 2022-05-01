from typing import Optional, List
from treenode import TreeNode

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        response = []

        if root:
            response += [root.val]

            if root.left:
                response += self.postorderTraversal(root.left)

            if root.right:
                response += self.postorderTraversal(root.right)

        return response

r1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
solution = Solution()
print(solution.postorderTraversal(root = r1))