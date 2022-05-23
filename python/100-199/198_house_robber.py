import sys
from typing import List, Set

class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = []
        i = len(nums) - 1

        while i >= 2:
            if self.rob(nums[:i-2]) + nums[i] >= self.rob(nums[:i-1]):
                houses.append(nums[i])
                i = i - 2
            else:
                i = i - 1

        if i == 1:
            if nums[0] > nums[1]:
                houses.append(nums[0])
            else:
                houses.append(nums[1])

        if i == 0:
            houses.append(nums[0])

        return sum(houses)




solution = Solution()
print(solution.rob(nums = [1,2,3,1]))