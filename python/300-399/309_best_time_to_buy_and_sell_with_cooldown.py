import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        has_cooldown = False
        profit = 0
        last_price = prices[0]

        for k in range(1, len(prices)):
            if prices[k] > last_price and not has_cooldown:
                profit = profit + prices[k] - last_price
                has_cooldown = True
                last_price = prices[k]
                continue

            last_price = prices[k]

            if has_cooldown:
                has_cooldown = False

        return profit


solution = Solution()
print(solution.maxProfit(prices = [1,2,3,0,2]))