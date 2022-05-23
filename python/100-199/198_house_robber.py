import sys
from typing import List, Set

class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = []
        i = len(nums) - 1

        while i >= 2:
            if self.rob(nums[:i-1]) + nums[i] >= self.rob(nums[:i]):
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
print(solution.rob(nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))