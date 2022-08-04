from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        local_minimum = None
        local_maximum = None
        response = 0

        for i in range(len(prices)):
            if local_minimum is None or local_minimum > prices[i]:
                if local_minimum is not None and local_maximum is not None and local_maximum > local_minimum:
                    response = response + local_maximum - local_minimum
                local_minimum = prices[i]
                local_maximum = prices[i]

            if local_maximum < prices[i]:
                local_maximum = prices[i]
                if i == len(prices) - 1 and local_maximum > local_minimum:
                    response = response + local_maximum - local_minimum

            if local_maximum > prices[i] and local_maximum > local_minimum:
                response = response + local_maximum - local_minimum
                local_minimum = prices[i]
                local_maximum = prices[i]

        return response

solution = Solution()
print(solution.maxProfit(prices = [2,4,1]))