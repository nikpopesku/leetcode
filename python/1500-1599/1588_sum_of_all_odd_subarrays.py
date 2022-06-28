from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) <= 2:
            return sum(arr)
        elif len(arr) == 3:
            return sum(arr) * 2

        numb = len(arr) // 2 if len(arr) / 2 > len(arr) // 2 else (len(arr) // 2) - 1

        sum_all = 0
        for i in range(len(arr)):
            if len(arr) % 2 == 1:
                numb = numb + 1 if i <= len(arr) / 2 else numb - 1
            elif not ((i == len(arr) // 2) and len(arr) % 2 == 0):
                numb = numb + 1 if (i + 1) <= len(arr) / 2 else numb - 1
            sum_all += arr[i] * numb


        return sum_all

solution = Solution()
print(solution.sumOddLengthSubarrays(arr = [1,1,1,1,1,1]))