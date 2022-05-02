from typing import Optional, List
from treenode import TreeNode

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        response = self.postorderTraversal(root.left) if root and root.left else []
        response += self.postorderTraversal(root.right) if root and root.right else []
        response += [root.val] if root else []

        return response

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        elif root.left and not root.right or root.right and not root.left:
            return False
        elif not root.left and not root.right:
            return True

        return self.postorderTraversal(root.left) == self.postorderTraversal(root.right)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.isSymmetric(root = root))