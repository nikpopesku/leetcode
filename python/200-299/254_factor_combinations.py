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
                    new_comb = combination[:pos] + [i] + combination[pos:]
                    exists = False

                    for c in results:
                        if c[:len(new_comb)] == tuple(new_comb):
                            exists = True
                            break

                    if not exists:
                        backtrack(div_res, div_res, new_comb)

            return results

        backtrack(n, n // 2, [])

        return results


solution = Solution()
print(solution.getFactors(n = 12))