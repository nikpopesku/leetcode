from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        total = 0
        counter = 1
        delta = []
        delta.append(None)

        for i in range(1, len(nums)):
            delta.append(nums[i] - nums[i - 1])

        delta[0] = delta[1]

        for i in range(1, len(delta)):
            if delta[i] == delta[i - 1]:
                counter += 1
            else:
                if counter >= 3:
                    total += (counter - 1) * (counter - 2) / 2

                counter = 1

        if counter >= 3:
            total += (counter - 1) * (counter - 2) / 2

        return int(total)




solution = Solution()
print(solution.numberOfArithmeticSlices(nums = [1,2,3,8,9,10]))