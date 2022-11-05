import sys
from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        response = []
        index = 0
        temp = 0
        while index < len(a) and index < len(b):
            whole, remainder = divmod(int(a[index]) + int(b[index]), 2)
            response.append(remainder + temp)
            temp = whole
            index = index + 1

        if len(a) != len(b):
            bigger = a if len(a) > len(b) else bigger
            while index < len(bigger):
                whole, remainder = divmod(int(bigger[index]) + temp, 2)
                response.append(remainder)
                temp = whole
                index = index + 1
        if temp > 0:
            whole, remainder = divmod(temp, 2)
            response.append(remainder)
            if whole > 0:
                response.append(remainder)

        return ''.join(str(c) for c in response[::-1])

solution = Solution()
print(solution.addBinary("1010", b = "1011"))