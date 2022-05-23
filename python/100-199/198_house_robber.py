import sys
from typing import List, Set

class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = []
        i = len(nums) - 1

        while i >= 2:
            if nums[i-2] + nums[i] >= nums[i-1]:
                houses.append(nums[i])
                i = i - 2
            else:
                i = i - 1

        if i == 1:
            houses.append(nums[i])

        return sum(houses)




solution = Solution()
print(solution.rob(nums = [1,2,3,1]))