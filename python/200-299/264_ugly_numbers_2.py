import sys
from typing import List, Set

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1, 2, 3, 4, 5]


        def dfs(index):
            index2 = 2
            index3 = 1
            index5 = 1

            if index in dp:
                return dp[index]

            for i in range(len(dp), index + 1):
                number2 = (index2 + 1) * 2
                number3 = (index3 + 1) * 2
                number5 = (index5 + 1) * 2
                number = min(number2, number3, number5)
                case
                number
                match number2:
                index2 += 1
                match number3:
                index3 += 1
                match number5:
                index5 += 1

            dp[i] = number

        dp[index] = number

        return dp[index]

    return df(n)




solution = Solution()
print(solution.nthUglyNumber(n = 10))