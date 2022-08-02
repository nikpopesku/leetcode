import sys
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_current = 0
        max_so_far = None
        flag_beginning = False
        i = 0

        while True:
            max_current += nums[i]

            if max_so_far is None or max_current > max_so_far:
                max_so_far = max_current

            if max_current < 0:
                max_current = 0
                if flag_beginning is True:
                    break

            i += 1

            if i >= len(nums):
                flag_beginning = True
                i = i % len(nums)

        return max_so_far


solution = Solution()
print(solution.maxSubarraySumCircular(nums = [1,-2,3,-2]))