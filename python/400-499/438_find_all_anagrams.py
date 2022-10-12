from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = len(s) - len(p)
        response = []
        hashmap_initial = {}

        for c in p:
            hashmap_initial[c] = (0 if c not in hashmap_initial else hashmap_initial[c]) + 1
        hashmap = hashmap_initial.copy()

        for i in range(len(s) - 1, -1, -1):
            if s[i] not in hashmap:
                counter = i - len(p) + 1
                if counter < 0:
                    break
                if len(hashmap) == 0:
                    hashmap = hashmap_initial.copy()
            if s[i] in hashmap:
                hashmap[s[i]] -= hashmap[s[i]]
                if hashmap[s[i]] == 0:
                    del hashmap[s[i]]
                if len(hashmap) == 0:
                    response.append(counter)

        return response




solution = Solution()
print(solution.findAnagrams(s = "abab", p = "ab"))