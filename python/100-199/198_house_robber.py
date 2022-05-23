import sys
from typing import List, Set

class Solution:
    houses = {}

    def rob(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1:
            return nums[0]

        if length == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]

        self.houses[1] = nums[0]
        self.houses[2] = nums[0] if nums[0] > nums[1] else nums[1]

        for i in range(3, length+1):
            self.houses[i] = max(self.houses[i-2] + nums[i-1], self.houses[i-1])

        return self.houses[length]





solution = Solution()
print(solution.rob(nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))