import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = float("-inf"), 0

        for price in prices:
            buy, sell = max(buy, sell - price), max(sell, buy + price - fee)

        return sell


solution = Solution()
print(solution.maxProfit(prices = [1,3,9], fee = 2))