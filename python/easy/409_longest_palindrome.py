import sys


class Solution:
    def longestPalindrome(self, s: str) -> int:
        left = []
        right = []
        without_pair = {}
        for key in s:
            if key not in without_pair:
                without_pair[key] = key
            else:
                left.insert(0, key)
                right.append(key)
                del without_pair[key]


        return len(left) + (1 if len(without_pair) >= 1 else 0) + len(right)




solution = Solution()
print(solution.longestPalindrome(sys.argv[1]))