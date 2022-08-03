import sys
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxstart = values[1] + 1
        max_place = 1

        for i in range(2, len(values) - 1):
            if values[i] > maxstart:
                maxstart = values[i] + i
                max_place = i

        maxend1 = None
        for j in range(max_place + 1, len(values)):
            if maxend1 is None or maxend1 < values[j] - j:
                maxend1 = values[j] - j

        maxend2 = None
        for j in range(max_place):
            if maxend2 is None or maxend2 < values[j] + j:
                maxend2 = values[j] + j


        if maxend1 is None:
            return maxend2 + maxstart - max_place * 2

        if maxend2 is None:
            return maxstart + maxend1

        return max(maxstart + maxend1, maxend2 + maxstart - max_place * 2)


solution = Solution()
print(solution.maxScoreSightseeingPair(values = [1,2]))