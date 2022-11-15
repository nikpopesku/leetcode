from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return 0

        before_last = last = (headID,)
        manager_map = {i: manager[i] for i in range(len(manager))}
        max_time = 0
        time = (0,)

        while last:
            last = tuple(k for k,v in manager_map.items() if v in before_last)
            if last:
                time = tuple(informTime[manager[i]] + time[before_last.index(manager[i])] for i in last)
                before_last = last
                max_time = max(max_time, max(time))

        return max_time

solution = Solution()
print(solution.numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]))