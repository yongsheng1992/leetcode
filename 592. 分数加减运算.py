from collections import deque
import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerators = []
        denominators = []

        cnt = 0
        stack2 = []
        temp = []
        for char in expression:
            if char == "/":
                cnt += 1
                stack2.append(int("".join(temp)))
                temp.clear()
            elif char == "-":
                if temp:
                    stack2.append(int("".join(temp)))
                    temp.clear()
                temp.append(char)
            elif char == "+":
                stack2.append(int("".join(temp)))
                temp.clear()
            else:
                temp.append(char)

        stack2.append(int("".join(temp)))

        while cnt != 0:
            cnt -= 1
            denominator = stack2.pop()
            numerator = stack2.pop()
            denominators.append(denominator)
            numerators.append(numerator)

        lcm = self.lcm_multiple(*denominators)

        for idx, numerator in enumerate(numerators):
            numerators[idx] = numerator * (lcm // denominators[idx])

        numerator = sum(numerators)
        gcd = self.gcd(numerator, lcm)

        print("{}/{}".format(numerator//gcd, lcm//gcd))
        return "{}/{}".format(numerator//gcd, lcm//gcd)

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def lcm(self, a, b):
        if a < b:
            b, a = a, b
        return a*b // self.gcd(a,b)

    def lcm_multiple(self, *nums):
        lcm = 1
        for num in nums:
            lcm = lcm * num // self.gcd(lcm, num)
        return lcm


if __name__ == "__main__":
    solution = Solution()
    solution.fractionAddition(expression = "-1/2+1/2")
    solution.fractionAddition(expression="-1/2+1/2+1/3")
    solution.fractionAddition(expression="1/3-1/2")


