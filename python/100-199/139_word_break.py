from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        response = False

        for word in wordDict:
            if s[:len(word)] == word:
                if len(word) == len(s) | response:
                    return True
                response = response | self.wordBreak(s[len(word):], wordDict)
                if response:
                    return True

        return response


solution = Solution()
print(solution.wordBreak(s = "leetcode", wordDict = ["leet","code"]))