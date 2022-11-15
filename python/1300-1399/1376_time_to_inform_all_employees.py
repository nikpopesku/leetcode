from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return 0

        queue = [headID]
        manager_map = {i: manager[i] for i in range(len(manager))}
        max_time = 0
        times = {headID: 0}

        while queue:
            element = queue.pop(0)
            temp = []
            for k, v in manager_map.items():
                if v == element:
                    temp.append(k)
                    queue.append(k)
                    times[k] = informTime[v] + times[v]
            for l in temp:
                del manager_map[l]


        return max(max_time, *times.values())

solution = Solution()
print(solution.numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]))