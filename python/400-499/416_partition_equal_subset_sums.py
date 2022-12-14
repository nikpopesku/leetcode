from typing import List, Dict

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False

        target = sum(nums)

        if target % 2 == 1:
            return False

        memo = {}

        return Solution.calc(target // 2, nums, memo)

    @staticmethod
    def calc(target: int, nums: List[int], memo: Dict[int, bool]) -> bool:
        if target in memo:
            return memo[target]

        for i in range(len(nums)):
            if Solution.calc(target - nums[i], nums[:i] + nums[i + 1:], memo):
                memo[target - nums[i]] = Solution.calc(target - nums[i], nums, memo)

                return memo[target - nums[i]]

        memo[target] = False

        return memo[target]





solution = Solution()
print(solution.canPartition(nums = [1,5,11,5]))