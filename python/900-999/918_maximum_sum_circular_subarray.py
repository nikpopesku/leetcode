import sys
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if all(num <= 0 for num in nums):
            return max(nums)

        overall_max, overall_min = float('-inf'), float('inf')
        max_ending_here, min_ending_here = 0, 0

        for num in nums:
            max_ending_here = max(max_ending_here, 0) + num  # if previous max negative, set to zero
            min_ending_here = min(min_ending_here, 0) + num  # if previous min positive, set to zero

            overall_max = max(overall_max, max_ending_here)
            overall_min = min(overall_min, min_ending_here)

        return max(overall_max, sum(nums) - overall_min)


solution = Solution()
print(solution.maxSubarraySumCircular(nums = [-3,-2,-3]))