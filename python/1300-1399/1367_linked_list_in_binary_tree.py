
from typing import Optional
from listnode import ListNode
from treenode import TreeNode


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        response = False

        if root and head and root.val == head.val:
            response = True

        if root.left:
            xxx = head.next if response else head
            response = self.isSubPath(xxx, root.left)

        if not response and root.right:
            xxx = head.next if response else head
            response = self.isSubPath(xxx, root.right)

        return response

listNode = ListNode(1, ListNode(4, ListNode(2)))
root = TreeNode(1, TreeNode(4, None, TreeNode(2, TreeNode(1))), TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(1), TreeNode(3)))))
solution = Solution()
print(solution.isSubPath(head = listNode, root = root))