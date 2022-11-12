import sys
from typing import List


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = [int(x) for x in list(str(n))]

        i = len(str(n)) - 1
        while min(digits[:i + 1]) == digits[i] and i > 0:
            i = i - 1

        if i == 0:
            return -1

        j = i - 1
        while digits[j:i + 1] == sorted(digits[j:i + 1], reverse=True) and j > 0:
            j = j - 1
        temp = sorted(digits[j:i + 1], reverse=True)
        k = 0
        minimum = temp
        while minimum >= digits[j:i + 1] and k < len(temp) - 1:
            temp = minimum
            minimum = sorted(temp, reverse=True)[:k + 1] + sorted(temp[k + 1:])
            k = k + 1

        elem = int(''.join(str(x) for x in digits[:j] + temp + digits[i+1:]))
        return elem if elem <= 2 ** 31 else -1


solution = Solution()
print(solution.nextGreaterElement(n = 2147483476))