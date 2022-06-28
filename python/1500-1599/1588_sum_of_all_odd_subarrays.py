from typing import List



class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        numb = (len(arr) // 2) + 1 if len(arr) / 2 > len(arr) // 2 else len(arr) // 2

        sum_all = 0
        for i in range(len(arr)):
            sum_all += arr[i] * numb
            numb = numb + 1 if (i + 1) < len(arr) / 2 else numb - 1

        return sum_all


solution = Solution()
print(solution.sumOddLengthSubarrays(arr = [1,2]))