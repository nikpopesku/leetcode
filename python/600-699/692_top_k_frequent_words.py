from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter()
        for word in words:
            cnt[word] += 1

        return [word for word, value in cnt.most_common(k)]





solution = Solution()
print(solution.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))