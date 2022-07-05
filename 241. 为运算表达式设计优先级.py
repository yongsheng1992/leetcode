from typing import List

"""
expression = "2*3-4*5
"""

class Solution:
    OP_SET = ("+", "-", "*")

    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        res = []
        for i, char in enumerate(expression):
            if char in self.OP_SET:
                left = self.diffWaysToCompute(expression[0:i])
                right = self.diffWaysToCompute(expression[i+1:])

                for x in left:
                    for y in right:
                        if char == "+":
                            res.append(x+y)
                        elif char == "-":
                            res.append(x-y)
                        else:
                            res.append(x*y)
        return res

    # def solve(self, expression: List, ans: List):
    #     print("exp", expression)
    #     if len(expression) == 1:
    #         ans.append(int(expression[0]))
    #     for i in range(len(expression)):
    #         if expression[i] in self.OP_SET:
    #             c = self.cal(expression[i-1], expression[i+1], expression[i])
    #             self.solve(expression[:i-1] + [str(c)] + expression[i+2:], ans)


if __name__ == "__main__":
    solution = Solution()
    print(solution.diffWaysToCompute("2*3-4*5"))
    print(solution.diffWaysToCompute("2-1-1"))
