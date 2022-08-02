import sys
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_current = 0
        max_so_far = None
        flag_beginning = False
        i = 0
        start_step = 0

        while True:
            max_current += nums[i]

            if i == start_step and flag_beginning is True:
                break

            if max_so_far is None or max_current > max_so_far:
                max_so_far = max_current

            i += 1

            if i >= len(nums):
                flag_beginning = True
                i = i % len(nums)

            if max_current < 0 or nums[i] < 0:
                max_current = 0
                start_step = i

        return max_so_far


solution = Solution()
print(solution.maxSubarraySumCircular(nums = [-3,-2,-3]))