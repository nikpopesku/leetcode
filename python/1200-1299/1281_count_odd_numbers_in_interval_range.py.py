from typing import List


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum, product = 0, 1
        l = list(str(n))
        while l:
            digit = int(l.pop())
            product *= digit
            sum += digit

        return product - sum

solution = Solution()
print(solution.subtractProductAndSum(n = 234))