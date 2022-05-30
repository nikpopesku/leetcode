from typing import List
from functools import reduce


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        counter = len(nums) - 1
        candidates = [nums[counter - 2], nums[counter - 1], nums[counter]]

        while not self.check(candidates):
            candidates.sort()
            candidates.pop()
            nums.pop()

    def check(self, nums: List[int]):
        maximum = max(nums)
        return nums[0] + nums[1] + nums[2] if nums[0] + nums[1] + nums[2] - maximum > maximum else 0


solution = Solution()
print(solution.largestPerimeter(nums = [2,1,2]))