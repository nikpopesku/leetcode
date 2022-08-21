import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell, prev_sell = float("-inf"), 0, 0

        for i, price in enumerate(prices):
            buy = max(buy, prev_sell - price - fee)
            prev_sell = sell
            sell = max(sell, buy + price - fee)

        return sell


solution = Solution()
print(solution.maxProfit(prices = [1,3,2,8,4,9], fee = 2))