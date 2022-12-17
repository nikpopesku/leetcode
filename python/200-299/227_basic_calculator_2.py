import operator

class Solution:
    def calculate(self, s: str) -> int:
        stack = list(s)
        reversed(stack)

        return Solution.expression(stack)

    @staticmethod
    def expression(stack):
        for i in range(len(stack)):
            if stack[i] == '+':
                return operator.add(Solution.expression(stack[:i]), Solution.expression(stack[i + 1:]))
            elif stack[i] == '-':
                return operator.sub(Solution.expression(stack[:i]), Solution.expression(stack[i + 1:]))
            elif stack[i] == '*':
                return operator.mul(Solution.expression(stack[:i]), Solution.expression(stack[i + 1:]))
            elif stack[i] == '/':
                return operator.floordiv(Solution.expression(stack[:i]), Solution.expression(stack[i + 1:]))

        return int(''.join(stack))


solution = Solution()
print(solution.calculate(s = "1-1+1"))