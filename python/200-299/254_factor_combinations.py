from typing import List

class Solution:
    def getFactors(self, n: int):
        results = set()

        def backtrack(target: int, limit: int, combination: List[int]):
            if target == 1:
                sort_comb = tuple(sorted(combination))
                if sort_comb not in results:
                    results.add(sort_comb)

            for i in range(2, limit + 1):
                if target % i == 0:
                    combination.append(i)
                    div_res = int(target / i)
                    backtrack(div_res, div_res, combination)
                    combination.pop()

            return results

        backtrack(n, n // 2, [])

        return results


solution = Solution()
print(solution.getFactors(n = 12))