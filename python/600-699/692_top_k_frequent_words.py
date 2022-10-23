from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter()
        for word in words:
            cnt[word] += 1

        min_value = min(value for word, value in cnt.most_common(k))
        big_words = [word for word, value in cnt.items() if value > min_value]
        if len(big_words) == k:
            return big_words

        equal_words = [word for word, value in cnt.items() if value == min_value]

        if len(equal_words) == k - len(big_words):
            return big_words + equal_words

        equal_words.sort()

        return big_words + equal_words[:k-len(big_words)]





solution = Solution()
print(solution.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 3))