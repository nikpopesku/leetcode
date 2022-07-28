from typing import List


class Solution:
    visited = {}

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        possible_combinations = [i for i in range(1, len(arr)+1) if i % 2 == 1]

        response = 0

        for length in possible_combinations:
            for i in range(len(arr)):
                if i + length <= len(arr):
                    response = response + sum(arr[i:i+length])

        return response

solution = Solution()
print(solution.sumOddLengthSubarrays(arr = [1,4,2,5,3]))
xxx = 6