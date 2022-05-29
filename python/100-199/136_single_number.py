from functools import reduce
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)


solution = Solution()
print(bin(solution.singleNumber(nums = [2,2,1])))