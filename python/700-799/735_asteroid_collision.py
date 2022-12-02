from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            stack.append(asteroid)

            if len(stack) < 2:
                continue

            change = True

            while len(asteroids) >= 2 and change:
                current_asteroid = stack[-1]
                previous_asteroid = stack[-2]

                if (previous_asteroid > 0) != (current_asteroid > 0):
                    change = False

                    if abs(previous_asteroid) < abs(current_asteroid):
                        stack.pop()
                        stack.pop()
                        stack.append(current_asteroid)
                        change = True
                    elif abs(previous_asteroid) == abs(current_asteroid):
                        stack.pop()
                        stack.pop()
                    else:
                        stack.pop()
                else:
                    change = False

        return stack





solution = Solution()
print(solution.asteroidCollision(asteroids = [5,10,-5]))
print('xxxx')