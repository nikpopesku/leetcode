from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        numberKeys = 0
        stack = []
        minSteps = float('inf')

        for row in range(m):
            for col in range(n):
                if grid[row][col].isalnum() and grid[row][col].islower():
                    numberKeys += 1
                if grid[row][col] == '@':
                    stack = [(row, col, 0, '', {(row, col)})]

        while stack:
            x, y, steps, keys, visited = stack.pop()
            if steps >= minSteps:
                continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#' and (nx, ny) not in visited:
                    if grid[nx][ny].isupper() and grid[nx][ny].lower() not in keys:
                        continue
                    if grid[nx][ny].islower() and grid[nx][ny] not in keys:
                        stack.append((nx, ny, steps + 1, keys + grid[nx][ny], {(nx, ny)}))
                        if len(keys + grid[nx][ny]) == numberKeys:
                            minSteps = min(minSteps, steps + 1)
                    else:
                        stack.append((nx, ny, steps + 1, str(keys), visited | {(nx, ny)}))

        return minSteps if minSteps < float('inf') else -1



solution = Solution()
grid = ["###.D.B.F.","..#b......","##....#..#","....@..#..","#d.AE.##c#",".....##.f.","#........C","..a#.#....","#....#e..#","........##"]
print(solution.shortestPathAllKeys(grid))
