import sys
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        previous = None
        unique = 0

        for element in nums:
            if element != previous:
                unique += 1
            elif previous == None:
                previous = element
                nums[unique] = element
                unique += 1

        return unique


solution = Solution()
print(solution.removeDuplicates([int(x) for x in sys.argv[1:]]))