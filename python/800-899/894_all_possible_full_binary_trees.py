from typing import Optional, List
from treenode import TreeNode

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        response = []
        i = 1
        intermediate_head = None
        while i <= n:
            node = TreeNode()
            if i == 1:
                intemediate_head = node
                i = i + 1

            if i < n - 1:
                node.left = TreeNode()
                node.right = TreeNode()
                i = i + 2

        return response

solution = Solution()
print(solution.allPossibleFBT(n = 7))
