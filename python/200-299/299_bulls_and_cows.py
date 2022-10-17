import sys
from typing import List, Set

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_map = {}

        for key, char in enumerate(secret):
            secret_map[char] = set() if char not in secret_map else secret_map[char]
            secret_map[char].add(key)

        bulls = 0
        cows = 0
        possible_cows = []

        for key, char in enumerate(guess):
            if char in secret_map:
                if key in secret_map[char]:
                    bulls += 1
                    secret_map[char] = secret_map[char] - {key}
                    if len(secret_map[char]) == 0:
                        del secret_map[char]
                else:
                    possible_cows.append(char)

        for char in possible_cows:
            if char in secret_map:
                secret_map[char].pop()
                cows += 1
                if len(secret_map[char]) == 0:
                    del secret_map[char]

        return str(bulls) + 'A' + str(cows) + 'B'




solution = Solution()
print(solution.getHint(secret = "011", guess = "110"))