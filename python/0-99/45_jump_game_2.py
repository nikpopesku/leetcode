import sys
from typing import List, Set

class Solution:
    def jump(self, nums: List[int]) -> int:
        start, end = 0, 1
        max_index = 0
        step = 0


        while True:
            for k in range(start, end):
                if nums[k] + k > max_index:
                    step = step + 1
                    max_index = nums[k] + k

                if max_index >= len(nums) - 1:
                    return step

                start, end = end, max_index + 1




solution = Solution()
print(solution.jump(nums = [1]))