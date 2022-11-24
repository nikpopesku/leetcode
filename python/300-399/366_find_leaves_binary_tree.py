
import sys
from typing import List
from typing import Optional
from treenode import TreeNode


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        response = []
        before_last = []
        last = Solution.findLeavesInternal(root, before_last)

        while last:
            response.append(last)
            last, before_last = Solution.findLeavesInternal(root, before_last), last

        return response

    @staticmethod
    def findLeavesInternal(root: Optional[TreeNode], before_last: List[int]) -> List:
        stack = [root]
        temp = []

        while stack:
            element = stack.pop()
            pushed = False
            if element.left and element.left.val not in before_last:
                stack.append(element.left)
                pushed = True
            if element.right and element.right.val not in before_last:
                stack.append(element.right)
                pushed = True
            if not pushed and element.val not in before_last:
                temp.append(element.val)

        return temp

solution = Solution()
print(solution.findLeaves(root=TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))