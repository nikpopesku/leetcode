from typing import List
from functools import reduce


class Solution:
    def freqAlphabets(self, s: str) -> str:
        hashmap = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i'}
        for i in range(10, 27):
            hashmap[str(i) + '#'] = chr(ord('j') + i - 10)

        lengths = set([len(i) for i in hashmap.values()])
        answer = []
        i = 0
        while i < len(s):
            for length in lengths:
                if (i + length) <= len(s) and s[i:i+length] in hashmap.keys():
                    element = hashmap[s[i:i+length]]
                    break
            else:
                length = 1
                element = s[i]
            answer.append(element)
            i = i + length

        return ''.join(answer)

solution = Solution()
print(solution.freqAlphabets(s = "10#11#12"))