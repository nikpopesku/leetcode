import sys
from typing import List, Set

class Solution:
    houses = {}

    def rob(self, nums: List[int]) -> int:
        length = len(nums)

        if length - 1 in self.houses:
            return self.houses[length - 1]

        i = length - 1

        if i == 1:
            if 1 not in self.houses:
                self.houses[1] = nums[0] if nums[0] > nums[1] else nums[0]
            return self.houses[1]

        if i == 0:
            if 0 not in self.houses:
                self.houses[0] = nums[0]
            return self.houses[0]

        if length - 1 not in self.houses:
            self.houses[length - 1] = self.rob(nums[:i - 1]) + nums[i] if self.rob(nums[:i - 1]) + nums[i] >= self.rob(nums[:i]) else self.rob(nums[:i])

        return self.houses[length - 1]




solution = Solution()
print(solution.rob(nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))