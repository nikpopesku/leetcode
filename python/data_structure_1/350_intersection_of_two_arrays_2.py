from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {}
        response = []

        for key, num in enumerate(nums1):
            hash[num] = (hash[num] if num in hash else 0) + 1

        for key, num in enumerate(nums2):
            if num in hash and hash[num] > 0:
                response.append(num)
                hash[num] -= 1


        return response



solution = Solution()
print(solution.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))