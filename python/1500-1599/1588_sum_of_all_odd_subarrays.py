from typing import List


class Solution:
    visited = {}

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) >= 2:
            sumall = 0

            if len(arr) % 2 == 1 and tuple(arr) not in self.visited:
                self.visited[tuple(arr)] = sum(arr)
                sumall = sum(arr)

            intermediate_sum = 0

            for i in range(len(arr)):
                elementlist = ([] if i == 0 else arr[:i]) + ([] if i == len(arr) - 1 else arr[i+1:])
                if tuple(elementlist) not in self.visited.keys():
                    intermediate_sum = intermediate_sum + self.sumOddLengthSubarrays(elementlist)

            return sumall + intermediate_sum
        else:
            if tuple(arr) not in self.visited:
                self.visited[tuple(arr)] = sum(arr)
                return arr[0]
            else:
                return 0

solution = Solution()
print(solution.sumOddLengthSubarrays(arr = [1,4,2,5,3]))
xxx = 6