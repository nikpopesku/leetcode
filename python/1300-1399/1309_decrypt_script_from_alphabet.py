from typing import List
from functools import reduce


class Solution:
    def freqAlphabets(self, s: str) -> str:
        hashmap = {'()': 'o', '(al)': 'al'}
        lengths = [len(i) for i in hashmap.values()]
        answer = []
        i = 0
        while i < len(s):
            for length in lengths:
                if (i + length) <= len(s) and s[i:i+length] in hashmap.keys():
                    element = hashmap[s[i:i+length]]['value']
                    break
            else:
                length = 1
                element = s[i]
            answer.append(element)
            i = i + length

        return ''.join(answer)

solution = Solution()
print(solution.freqAlphabets(s = "10#11#12"))