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
            if target - nums[i] > 0:
                attempt = Solution.calc(target - nums[i], nums[:i] + nums[i + 1:], memo)
                if attempt:
                    memo[target - nums[i]] = attempt

                    return memo[target - nums[i]]
            elif target - nums[i] == 0:
                memo[target] = True

                return memo[target]

        memo[target] = False

        return memo[target]





solution = Solution()
print(solution.canPartition(nums = [1,5,11,5]))