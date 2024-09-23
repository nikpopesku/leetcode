from typing import List
from collections import defaultdict

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x: x[-1])
        totalCost = 0
        totalEdges = 0
        counter = 0
        mst = defaultdict(list)


        while totalEdges < n - 1:
            if counter > len(connections) - 1:
                break
            start, end, cost = connections[counter]
            prev, cur = None, start

            while cur in mst and cur != end:
                changed = False
                for nxt in mst[cur]:
                    if nxt != prev:
                        prev = cur
                        cur = nxt
                        changed = True
                    if changed:
                        break

                if not changed:
                    break

            if cur == end:
                continue

            totalCost += cost
            totalEdges += 1
            mst[start].append(end)
            mst[end].append(start)
            counter += 1

        return totalCost if totalEdges + 1 == n else -1

solution = Solution()
print(solution.minimumCost(n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]))