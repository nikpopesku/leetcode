from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        hashmap = {}

        for i in range(len(arr)):
            count_bits = 0
            element = arr[i]
            while element:
                count_bits = count_bits + (element & 1)
                element = element >> 1
            hashmap[count_bits] = [arr[i]] if count_bits not in hashmap.keys() else hashmap[count_bits] + [arr[i]]
        dict(sorted(hashmap.items()))

        response = []
        for v in hashmap.values():
            v.sort()
            response = response + v

        return response

solution = Solution()
print(solution.sortByBits(arr = [0,1,2,3,4,5,6,7,8]))