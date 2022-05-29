from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        minimum, maximum, sum = salary[0], salary[0], salary[0]

        for i in range(1, len(salary)):
            minimum = min(minimum, salary[i])
            maximum = max(maximum, salary[i])
            sum += salary[i]

        return round(((sum - minimum - maximum) / (len(salary) - 2)), 5)

solution = Solution()
print(solution.average(salary = [4000,3000,1000,2000]))