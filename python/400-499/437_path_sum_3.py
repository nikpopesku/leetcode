import collections
from typing import Optional
from treenode import TreeNode


class Solution(object):
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(sumHash, prefixSum, node):
            if not node:
                return 0

            # Sum of current path
            prefixSum += node.val

            # number of paths that ends at current node
            path = sumHash[prefixSum - targetSum]

            # add currentSum to prefixSum Hash
            sumHash[prefixSum] += 1

            # traverse left and right of tree
            path += dfs(sumHash, prefixSum, node.left) + dfs(sumHash, prefixSum, node.right)

            # remove currentSum from prefixSum Hash
            sumHash[prefixSum] -= 1

            return path

        # depth first search, initialize sumHash with prefix sum of 0, occurring once
        return dfs(collections.defaultdict(int, {0: 1}), 0, root)

solution = Solution()
print(solution.pathSum(root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11))), targetSum = 8))