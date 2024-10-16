from typing import List
from collections import defaultdict, Counter


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        inDegree = defaultdict(int)
        adj = defaultdict(list)

        for e in edges:
            if e[0] == e[1]:
                return -1
            inDegree[e[1]] += 1
            adj[e[0]].append(e[1])

        stack = [(i, str(colors[i])) for i in range(len(colors)) if inDegree[i] == 0]
        maxColors = 0
        visited = {i[0] for i in stack}

        while stack:
            newStack = []
            for elem, path in stack:
                maxColors = max(maxColors, Counter(path).most_common(1)[0][1])

                for nei in adj[elem]:
                    if nei in visited:
                        return -1
                    visited.add(nei)
                    newStack.append((nei, path + str(colors[nei])))

            stack = newStack

        return maxColors



solution = Solution()
print(solution.largestPathValue(colors = "rrrde", edges = [[4,2],[3,4],[0,3],[1,0],[2,1]]))