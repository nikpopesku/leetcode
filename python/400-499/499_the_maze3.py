from typing import List
from heapq import heappop, heappush


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        directions = {'d': (1, 0), 'u': (-1, 0), 'r': (0, 1), 'l': (0, -1)}
        pq = [(0, tuple(ball), '')]
        minDistance = float('inf')
        minInstruction = 'impossible'

        while pq:
            distance, node, instruction = heappop(pq)
            x, y = node
            if distance > m * n:
                return minInstruction
            
            for instr, direction in directions.items():
                dx, dy = direction
                counter = 0
                nx, ny = x, y
                while 0 <= nx + dx < m and 0 <= ny + dy < n and maze[nx + dx][ny + dy] == 0:
                    counter += 1
                    nx, ny = dx + nx, dy + ny
                    if nx == hole[0] and ny == hole[1]:
                        if minDistance > distance + counter:
                            minDistance = distance + counter
                            minInstruction = instruction + instr
                        elif minDistance == distance + counter:
                            minInstruction = min(minInstruction, instruction + instr)

                if counter > 0 and distance + counter < minDistance:
                    heappush(pq, (distance + counter, (nx, ny), instruction + instr))

        return minInstruction


solution = Solution()
print(solution.findShortestWay(maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], ball = [4,3], hole = [0,1]))