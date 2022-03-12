import sys
from typing import List


class Solution:
    nodes = set()
    old_color = None
    new_color = None

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if self.old_color is None:
            self.old_color = image[sr][sc]
        if self.new_color is None:
            self.new_color = newColor
        if (sr, sc) not in self.nodes:
            if sr - 1 >= 0 and self.old_color == image[sr-1][sc] and image[sr][sc] in [self.new_color, self.old_color]:
                image[sr-1][sc] = newColor
            if sr + 1 <= len(image) - 1 and self.old_color == image[sr+1][sc] and image[sr][sc] in [self.new_color, self.old_color]:
                image[sr+1][sc] = newColor
            if sc - 1 >= 0 and self.old_color == image[sr][sc-1] and image[sr][sc] in [self.new_color, self.old_color]:
                image[sr][sc-1] = newColor
            if sc + 1 <= len(image) - 1 and self.old_color == image[sr][sc+1] and image[sr][sc] in [self.new_color, self.old_color]:
                image[sr][sc+1] = newColor
            if image[sr][sc] == self.old_color:
                image[sr][sc] = newColor
            self.nodes.add((sr, sc))

        if image[sr][sc] == self.new_color:
            if sr - 1 >= 0 and (sr-1, sc) not in self.nodes:
                self.floodFill(image, sr-1, sc, self.new_color)
            if sr + 1 <= len(image) - 1 and (sr + 1, sc):
                self.floodFill(image, sr + 1, sc, self.new_color)
            if sc - 1 >= 0 and (sr, sc-1) not in self.nodes:
                self.floodFill(image, sr, sc-1, self.new_color)
            if sc + 1 <= len(image) - 1 and (sr, sc+1):
                self.floodFill(image, sr, sc+1, self.new_color)


        return image



solution = Solution()
print(solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))
print('xxxx')