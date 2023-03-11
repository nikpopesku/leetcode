from typing import List

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        results = []

        def backtrack(target: int, limit: int, combination: List[int]):
            if target == 1:
                results.append(combination.copy())

            for i in range(2, limit + 1):
                if n % i == 0:
                    combination.append(i)
                    div_res = int(n / i)
                    backtrack(div_res, div_res, combination)

            return results

        return backtrack(n, n - 1, [])


solution = Solution()
print(solution.getFactors(n = 12))