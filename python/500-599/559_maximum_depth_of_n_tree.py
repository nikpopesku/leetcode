from ntreenode import Node


class Solution:
    def maxDepth(self, root: Node) -> int:
        queue = [[root]]

        response = 0

        while queue:
            elements = queue.pop(0)
            response = response + 1
            queue.append([child for element in elements for child in element.children])

        return response


solution = Solution()
print(solution.maxDepth(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])))