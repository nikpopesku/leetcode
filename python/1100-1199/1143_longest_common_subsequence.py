from typing import List
from functools import reduce


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_max = {}
        dp_min = {}

        min_length = min(len(text1), len(text2))
        min_text = text1 if len(text1) == min_length else text2
        max_text = text2 if min_text == text1 else text1

        min_so_far = float('inf')
        min_index = None

        for i in range(len(min_text)):
            index = max_text.find(min_text[i])
            if index != -1 and index < min_so_far:
                min_so_far = index
                min_index = i

        if min_so_far == float('inf'):
            return 0

        dp_max[0] = min_so_far
        dp_min[0] = min_index

        j = 0
        while j < len(min_text)-1:
            j += 1
            min_so_far = float('inf')
            min_index = None

            for i in range(dp_min[j - 1] + 1, len(min_text)):
                index = max_text.find(min_text[i], dp_max[j - 1] + 1)

                if index != -1 and index < min_so_far:
                    min_so_far = index
                    min_index = i

            if min_so_far == float('inf'):
                return max(dp_min.keys()) + 1

            dp_max[j] = min_so_far
            dp_min[j] = min_index

        return max(dp_min.keys()) + 1


solution = Solution()
print(solution.longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))