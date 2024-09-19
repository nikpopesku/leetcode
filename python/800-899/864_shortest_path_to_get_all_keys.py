from typing import List


class Solution:
    def __init__(self):
        self.grid = None

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        self.grid = grid
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        stack = self.start(m, n)
        response = 0
        numberKeys = 0
        keys = set()
        visited = set(stack)

        for row in range(m):
            for col in range(n):
                if grid[row][col].isalnum() and grid[row][col].islower():
                    numberKeys += 1

        while stack:
            newStack = set()
            for x, y in stack:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#' and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        if grid[nx][ny].isupper() and grid[nx][ny].lower() not in keys:
                            continue
                        if grid[nx][ny].islower() and grid[nx][ny] not in keys:
                            keys.add(grid[nx][ny])
                            visited = {(nx, ny)}
                        newStack.add((nx, ny))
            stack = newStack
            response += 1
            if len(keys) == numberKeys:
                break

        return response if len(keys) == numberKeys else -1

    def start(self, m: int, n: int):
        for row in range(m):
            for col in range(n):
                if self.grid[row][col] == '@':
                    return {(row, col)}

solution = Solution()
grid = ["@...a",".###A","b.BCc"]
print(solution.shortestPathAllKeys(grid))
