from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sumit = sum(piles)
        kmin = sumit // h

        begin, end = kmin, sumit

        def calit(k):
            response = 0
            for pile in piles:
                response += pile // k
                response += (1 if pile % k > 0 else 0)

            return response

        while begin < end:
            km = (begin + end) // 2

            if calit(km) == h and calit(km-1) > h:
                return km
            elif calit(km) <= h:
                end = km + 1
            else:
                begin = km

        return begin


solution = Solution()
print(solution.minEatingSpeed( piles = [3,6,7,11], h = 8))
