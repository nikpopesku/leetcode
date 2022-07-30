import sys
from typing import List, Set

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(nums[0] + self.deleteAndEarn([nums[j] for j in range(1, len(nums)) if nums[j] != nums[0] - 1 and nums[j] != nums[0] + 1]),
                   self.deleteAndEarn(nums[1:]))





solution = Solution()
print(solution.deleteAndEarn(nums = [3,4,2]))