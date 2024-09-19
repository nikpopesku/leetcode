from typing import List


class Solution:
    def __init__(self):
        self.grid = None

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        self.grid = grid
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        start = None

        stack = self.start(m, n)
        response = 0
        keys = set()
        visited = set(stack)

        while stack:
            newStack = []
            for x, y in stack:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#' and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        if grid[nx][ny].isupper() and grid[nx][ny].lower() not in keys:
                            continue
                        if grid[nx][ny].islower():
                            keys.add((nx, ny))
                            visited = {nx, ny}
                        newStack.append((nx, ny))
            stack = newStack
            response += 1

        return response

    def start(self, m: int, n: int):
        for row in range(m):
            for col in range(n):
                if self.grid[row][col] == '@':
                    return [(row, col)]

solution = Solution()
grid = ["@.a..","###.#","b.A.B"]
print(solution.shortestPathAllKeys(grid))
