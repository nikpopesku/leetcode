from typing import List
from itertools import permutations
from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        locations  = {v: (r, c) for r, rv in enumerate(grid) for c, v in enumerate(rv) if v not in '.#'}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        keys = ''.join([k for k in locations.keys() if 'a' <= k <= 'z'])
        response = float('inf')

        def bfs (source: str, target: str, keys: tuple):
            stack = [locations[source]]
            visited = set()
            steps = 0

            while stack:
                newStack = []

                for x, y in stack:
                    if x == locations[target][0] and y == locations[target][1]:
                        return steps
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#' and (nx, ny) not in visited:
                            if 'A' <= grid[nx][ny] <= 'Z' and grid[nx][ny].lower() not in keys:
                                continue
                            if 'a' <= grid[nx][ny] <= 'z' and grid[nx][ny].lower() in keys:
                                keys = keys + tuple(list(grid[nx][ny]))
                            newStack.append((nx, ny))

                steps += 1
                stack = newStack

            return float('inf')


        for cand in permutations(keys):
            pathLength = 0
            for i in range(len(cand)):
                source = cand[i-1] if i > 0 else '@'
                pathLength += bfs(source, cand[i], cand[:i])

                if pathLength > response or pathLength == float('inf'):
                    break
            else:
                response = pathLength

        return response if response < float('inf') else -1



solution = Solution()
grid = ["###.D.B.F.","..#b......","##....#..#","....@..#..","#d.AE.##c#",".....##.f.","#........C","..a#.#....","#....#e..#","........##"]
print(solution.shortestPathAllKeys(grid))
