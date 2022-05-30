from typing import List
from functools import reduce


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        counter = len(nums) - 1
        candidates = [nums[counter - 2], nums[counter - 1], nums[counter]]

        while not rule:
            candidates.sort()
            candidates.pop()
            nums.pop()


solution = Solution()
print(solution.largestPerimeter(nums = [2,1,2]))