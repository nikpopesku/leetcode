import sys
from typing import List, Set

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        possible_positions = list(range(nums[0] + 1))
        i = 1

        if possible_positions[-1] >= len(nums) - 1:
            return True

        if nums[0] == 0:
            return False

        while i >= 0:
            for j in range(1, nums[i] + 1):
                if j + i not in possible_positions:
                    possible_positions.append(j + i)
                    if j + i >= len(nums) - 1:
                        return True
                    i = len(possible_positions)
            i = i - 1

        return False



solution = Solution()
print(solution.canJump(nums = [1,1,1,0]))