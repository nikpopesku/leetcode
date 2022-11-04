
from typing import Optional
from listnode import ListNode
from treenode import TreeNode


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        response = Solution.check(head, root)

        if not response and root:
            response = self.isSubPath(head, root.left)

        if not response and root:
            response = self.isSubPath(head, root.right)

        return response

    @staticmethod
    def check(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root or not head or root.val != head.val:
            return False

        while root and head:
            if root.val == head.val:
                head = head.next

                if head is None:
                    return True

            if root.left and root.left.val == head.val:
                root = root.left
            elif root.right and root.right.val == head.val:
                root = root.right
            else:
                return False

        return False

listNode = ListNode(4, ListNode(2, ListNode(8)))
root = TreeNode(1, TreeNode(4, None, TreeNode(2, TreeNode(1))), TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(1), TreeNode(3)))))
solution = Solution()
print(solution.isSubPath(head = listNode, root = root))