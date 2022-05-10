from typing import Optional, List
from treenode import Node

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        return root


r1 = Node(1, None, Node(2, Node(3)))
solution = Solution()
print(solution.connect(root = r1))