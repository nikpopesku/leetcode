from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = len(s) - len(p) - 1
        response = []
        hashmap_initial = {}

        for c in p:
            hashmap_initial[c] = (0 if c not in hashmap_initial else hashmap_initial[c]) + 1
        hashmap = hashmap_initial.copy()

        for i in range(len(s) - 1, -1, -1):
            if s[i] not in hashmap or hashmap[s[i]] == 0:
                counter = i - len(p) - 1
                if counter < 0:
                    break
                hashmap = hashmap_initial.copy()
            else:
                hashmap[s[i]] -= hashmap[s[i]]
                if hashmap[s[i]] == 0:
                    del hashmap[s[i]]
                if len(hashmap) == 0:
                    response.append(counter)

        return response




solution = Solution()
print(solution.findAnagrams(s = "cbaebabacd", p = "abc"))