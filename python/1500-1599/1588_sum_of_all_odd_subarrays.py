from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) <= 2:
            return sum(arr)
        elif len(arr) == 3:
            return sum(arr) * 2
        elif len(arr) == 4:
            return sum(arr) + sum(arr[:3]) + sum(arr[1:4])

        numb = (len(arr) // 2) + 1 if len(arr) / 2 > len(arr) // 2 else len(arr) // 2

        sum_all = 0
        for i in range(len(arr)):
            sum_all += arr[i] * numb
            if i - 1 == len(arr) // 2 and len(arr) % 2 == 0:
                continue
            numb = numb + 1 if (i + 1) <= len(arr) / 2 else numb - 1

        return sum_all

solution = Solution()
print(solution.sumOddLengthSubarrays(arr = [1,1,1,1,1,1,1,1,1,1]))