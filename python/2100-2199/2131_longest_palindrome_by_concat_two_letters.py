from typing import List
import collections

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        collection_words = collections.Counter(words)
        counter = 0

        while collection_words:
            k = list(collection_words.keys())[0]

            if k[0] == k[1]:
                counter = counter + collection_words[k] * 2
            else:
                v2 = collection_words[k[::-1]] if k[::-1] in collection_words else 0
                counter = counter + min(collection_words[k], v2) * 4
                if v2:
                    del collection_words[k[::-1]]

            del collection_words[k]

        return counter

solution = Solution()
print(solution.longestPalindrome(words = ["lc","cl","gg"]))