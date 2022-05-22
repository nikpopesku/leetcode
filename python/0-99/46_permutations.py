import sys
from typing import List, Set

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute_all(offset, nums):
            if offset == len(nums) - 1:
                result.append(nums.copy())

            j = offset + 1
            while j < len(nums):
                nums[offset], nums[j] = nums[j], nums[offset]
                permute_all(j, nums)
                nums[j], nums[offset] = nums[offset], nums[j]
                j += 1


        result = []
        permute_all(0, [])
        return result





solution = Solution()
print(solution.permute(nums = [1,2,3]))