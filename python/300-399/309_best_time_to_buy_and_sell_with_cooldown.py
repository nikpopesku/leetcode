import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        profit, local_max, local_min = 0, prices[0], prices[0]
        has_cooldown = False

        for k in range(1, len(prices)):
            if prices[k] > local_max:
                local_max = prices[k]

            if prices[k] < local_max and not has_cooldown and local_max > local_min:
                profit = profit + local_max - local_min
                has_cooldown = True

            if prices[k] < local_min:
                local_min = prices[k]
                local_max = prices[k]

            if has_cooldown:
                has_cooldown = False

        return profit


solution = Solution()
print(solution.maxProfit(prices = [1,2,3,0,2]))