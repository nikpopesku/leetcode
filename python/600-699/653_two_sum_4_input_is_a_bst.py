from typing import Optional, List
from treenode import TreeNode

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return True


r1 = TreeNode(5, TreeNode(4), TreeNode(8, TreeNode(7, TreeNode(6)), TreeNode(9)))
solution = Solution()
print(solution.findTarget(root = r1))