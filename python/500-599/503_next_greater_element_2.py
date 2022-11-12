import sys
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        return [next(x for x in nums[i+1:] + nums[:i] if x > nums[i]) for i in range(len(nums))]


solution = Solution()
print(solution.nextGreaterElements(nums = [1,2,1]))