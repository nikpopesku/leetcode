from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right and nums[left] > nums[right]:
            i = (right - left) // 2
            if nums[left + i] > nums[left] and i > 0:
                left = i + left
            elif i > 0:
                right = i + left
            else:
                left = right

        if nums[0] <= target <= nums[left - 1]:
            return Solution.binary(nums[:left], target)

        if nums[left] <= target <= nums[-1]:
            return left + Solution.binary(nums[left:], target)

        return -1

    @staticmethod
    def binary(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (right - left) // 2
            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

        return left



solution = Solution()
solution.mergeTwoLists(list1 = l1, list2 = l2).print()