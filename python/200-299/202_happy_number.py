from typing import List
from functools import reduce


class Solution:
    def isHappy(self, n: int) -> bool:
        total_sum = 0
        trend_asc = 0
        trend_desc = 0
        while n // 10 != 0 and trend_desc < 10 and trend_asc < 10:
            previous_n = n
            while n:
                digit = n % 10
                n = n // 10
                total_sum += digit ** 2
            if total_sum == 1:
                return True
            elif previous_n < total_sum:
                trend_desc = 0
                trend_asc += 1
            else:
                trend_asc = 0
                trend_desc += 1
            n = total_sum


        return True if n == 1 else False

solution = Solution()
print(solution.isHappy(n = 19))