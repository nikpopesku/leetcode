from typing import List
from collections import defaultdict

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x: x[-1])
        cost = 0
        counter = 0
        mst = defaultdict(list)


        while len(mst) < 2 * (len(connections) - 1):
            start, end, c = connections[counter]
            prev, cur = None, start

            while cur in mst and cur != end:
                changed = False
                for nxt in mst[cur]:
                    if nxt != prev:
                        cur, last = nxt, cur
                        changed = True

                if not changed:
                    break

            if cur == end:
                continue

            cost += c
            mst[start].append(end)
            mst[end].append(start)
            counter += 1

        return cost

solution = Solution()
print(solution.minimumCost(n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]))