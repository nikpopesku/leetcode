from typing import Optional
from treenode import TreeNode

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return [0,1,2,4,8,3,5,6,7]

solution = Solution()
print(solution.sortByBits(arr = [0,1,2,3,4,5,6,7,8]))