import sys
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        response = []

        for i in range(len(nums)):
            try:
                response.append(next(x for x in nums[i + 1:] + nums[:i] if x > nums[i]))
            except StopIteration:
                response.append(-1)

        return response


solution = Solution()
print(solution.nextGreaterElements(nums = [1,2,1]))