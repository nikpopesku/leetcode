import sys
from typing import List, Set

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        return self.calculate(nums)

    def calculate(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        xxx1 = [nums[j] for j in range(1, len(nums)) if nums[j] < nums[0] - 1]
        xxx2 = nums[1:]

        return max(nums[0] + self.calculate([nums[j] for j in range(1, len(nums)) if nums[j] < nums[0] - 1]), self.calculate(nums[1:]))





solution = Solution()
print(solution.deleteAndEarn(nums = [2,2,3,3,3,4]))