from typing import List
from listnode import ListNode


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        last = 0
        return [last := last + num for num in nums]


solution = Solution()
print(solution.runningSum(nums = [1,2,3,4]))