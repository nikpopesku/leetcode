from typing import List
from collections import Counter

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
        freq = Counter(nums)
        pairs = [(num, count) for num, count in freq.items()]
        pairs.sort()

        used, not_used = 0, 0

        for i, (num, count) in enumerate(pairs):
            if i == 0 or pairs[i - 1][0] != num - 1:  # no previous noum or not num - 1
                not_used = max(used, not_used)  # choose max
                used = num * count + not_used  # add point from this num
            else:
                used, not_used = num * count + not_used, max(used, not_used)

        return max(used, not_used)

solution = Solution2()
print(solution.deleteAndEarn(nums = [8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4]))