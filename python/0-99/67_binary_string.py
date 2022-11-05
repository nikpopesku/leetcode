import sys
from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        response = []
        temp = 0
        smaller, bigger = a, b

        if len(a) != len(b):
            smaller = a if len(a) < len(b) else b
            bigger = a if len(a) > len(b) else b
            smaller = '0' * (len(bigger) - len(smaller)) + smaller

        index = len(smaller) -1

        while index >= 0:
            whole, remainder = divmod(int(a[index]) + int(b[index]), 2)
            response.append(remainder + temp)
            temp = whole
            index = index - 1

        if temp > 0:
            whole, remainder = divmod(temp, 2)
            response.append(remainder)
            if whole > 0:
                response.append(remainder)

        return ''.join(str(c) for c in response[::-1])

solution = Solution()
print(solution.addBinary("1010", b = "1011"))