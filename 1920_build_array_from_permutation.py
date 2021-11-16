class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        by_key = function(x):
            return nums[x]

        return nums.sort(key=by_key)