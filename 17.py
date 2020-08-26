"""
    17. 电话号码的字母组合
    --------------------
    简单的模拟即可。
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = mapping[digits[0]]

        for i in range(1, n):
            res = self.merge(res, mapping[digits[i]])

        return res

    def merge(self, a, b):
        res = []
        for i in range(len(a)):
            for j in range(len(b)):
                res.append(a[i]+b[j])
        return res
