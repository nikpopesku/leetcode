import sys
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxstart = values[0] + 0
        max_place = 0

        for i in range(1, len(values) - 1):
            if values[i] > maxstart:
                maxstart = values[i] + i
                max_place = i

        maxend = None
        for j in range(max_place + 1, len(values)):
            if maxend is None or maxend < values[j] - j:
                maxend = values[j] - j

        return maxstart + maxend


solution = Solution()
print(solution.maxScoreSightseeingPair(values = [8,1,5,2,6]))