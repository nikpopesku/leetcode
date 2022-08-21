from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            if s[:len(word)] == word:
                if len(word) == len(s):
                    return True
                return self.wordBreak(s[len(word):], wordDict)

        return False


solution = Solution()
print(solution.wordBreak(s = "leetcode", wordDict = ["leet","code"]))