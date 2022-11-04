from typing import Optional
from listnode import ListNode, create_single_linked_list


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        power = 1
        response = 0

        for char1 in num1[::-1]:
            temp = 0
            response_temp = []
            for char2 in num2[::-1]:
                whole, remainder = divmod(int(char1) * int(char2), 10)
                remainder = remainder + temp
                temp = whole
                response_temp.append(remainder)
            if temp != 0:
                response_temp.append(temp)

            response = response + int(''.join(str(c) for c in response_temp[::-1])) * power
            power = power * 10

        return str(response)



solution = Solution()
print(solution.multiply(num1 = "123", num2 = "456"))