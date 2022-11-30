from typing import Optional, List
from treenode import TreeNode

class Solution:
    response = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        stack = [(root, [])]
        response = []

        while stack:
            element, path = stack.pop()

            if element.val == targetSum and not element.left and not element.right:
                path[:].append(element.val)
                response.append(path)
            if element.left:
                path[:].append(element.val)
                stack.append((element.left, path))
            if element.right:
                path[:].append(element.val)
                stack.append((element.right, path))

        return response

r1 = TreeNode(-2, None, TreeNode(-3))
solution = Solution()
print(solution.hasPathSum(root = r1, targetSum = -5))