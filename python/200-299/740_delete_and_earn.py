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



class Solution2:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_points = {}

        for i in range(len(nums)):
            max_points[nums[i]] = nums[i] if nums[i] not in max_points else max_points[nums[i]] + nums[i]

        max_points = {k: v for k, v in sorted(max_points.items(), key=lambda item: item[1], reverse=True)}

        response = 0
        used = []

        for k,v in max_points.items():
            if k not in used:
                used.append(k+1)
                used.append(k-1)
                response = response + v

        return response

solution = Solution2()
print(solution.deleteAndEarn(nums = [3,4,2]))