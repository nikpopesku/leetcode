import sys
from typing import List, Set

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1, 2, 3, 4, 5]

        index2 = 2
        index3 = 1
        index5 = 1

        if n <= len(dp):
            return dp[n-1]

        while len(dp) < n:
            number2 = (index2 + 1) * 2
            number3 = (index3 + 1) * 3
            number5 = (index5 + 1) * 5
            number = min(number2, number3, number5)

            if number == number2:
                index2 += 1
            elif number == number3:
                index3 += 1
            else:
                index5 += 1

            if number in dp:
                continue

            copy_number = number

            for i in [2,3,5]:
                while divmod(number, i)[1] == 0:
                    number = divmod(number, i)[0]

            if number != 1:
                continue

            dp.append(copy_number)

        return dp[n-1]




solution = Solution()
print(solution.nthUglyNumber(n = 11))