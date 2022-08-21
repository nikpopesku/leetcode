from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        response = False

        for word in wordDict:
            if s[:len(word)] == word:
                n = 1
                while s[:len(word) * n] == word * n:
                    n += 1
                if len(word) * (n - 1) == len(s) | response:
                    return True
                response = response | self.wordBreak(s[len(word) * (n - 1):], wordDict)
                if response:
                    return True

        return response


solution = Solution()
print(solution.wordBreak(s = "catskicatcats", wordDict = ["cats","cat","dog","ski"]))