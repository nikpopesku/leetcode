from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        map = {}
        response = [None] * len(temperatures)

        for i in range(len(temperatures)):
            for key, value in map.items():
                if value[0] > temperatures[i]:
                    response[key] = value[1] + 1
                else:
                    map[key] = [map[key][0], map[key][1] + 1]
            map[i] = [temperatures[i], 0]

        if len(map) > 0:
            for key, value in map.items():
                response[key] = 0

        return response

solution = Solution()
print(solution.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))