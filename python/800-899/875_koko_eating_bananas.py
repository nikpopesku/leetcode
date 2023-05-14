from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sumit = sum(piles)
        kmin = sumit // h

        l, r = kmin, sumit

        def calit(k):
            response = 0
            for pile in piles:
                response += pile // k
                response += (1 if pile % k > 0 else 0)

            return response

        while l < r:
            m = (l + r) // 2

            if calit(m) == h and calit(m-1) > h:
                return m
            elif calit(m) < h:
                end = m + 1
            else:
                begin = m

        return l


solution = Solution()
print(solution.minEatingSpeed( piles = [3,6,7,11]))
