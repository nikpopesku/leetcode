from typing import List
from bisect import bisect_left

class Solution:
    def getFactors(self, n: int):
        if n == 1:
            return []

        results = set()

        def backtrack(target: int, limit: int, combination: List[int]):
            if target == 1 and tuple(combination) not in results:
                    results.add(tuple(combination))

            for i in range(2, limit + 1):
                if target % i == 0:
                    div_res = int(target / i)
                    pos = bisect_left(combination, i)
                    backtrack(div_res, div_res, combination[:pos] + [i] + combination[pos:])

            return results

        backtrack(n, n // 2, [])

        return results


solution = Solution()
print(solution.getFactors(n = 12))