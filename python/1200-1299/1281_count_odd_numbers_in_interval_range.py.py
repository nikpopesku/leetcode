from typing import List


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum, product = 0, 1
        while n:
            digit = n % 10
            n = n // 10
            product *= digit
            sum += digit

        return product - sum

solution = Solution()
print(solution.subtractProductAndSum(n = 234))