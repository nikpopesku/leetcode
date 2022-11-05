import sys
from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        response = []
        temp = 0

        if len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a

        if len(b) < len(a):
            b = '0' * (len(a) - len(b)) + b

        index = len(a) - 1

        while index >= 0:
            whole, remainder = divmod(int(a[index]) + int(b[index]) + temp, 2)
            response.append(remainder)
            temp = whole
            index = index - 1

        if temp > 0:
            whole, remainder = divmod(temp, 2)
            response.append(remainder)
            if whole > 0:
                response.append(remainder)

        return ''.join(str(c) for c in response[::-1])

solution = Solution()
print(solution.addBinary(a = "11", b = "1"))