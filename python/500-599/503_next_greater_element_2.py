import sys
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        return [([x for x in nums[i + 1:] if x > nums[i]] or [x for x in nums[:i] if x > nums[i]] or [-1])[0] for i in range(len(nums))]


solution = Solution()
print(solution.nextGreaterElements(nums = [1,2,1]))