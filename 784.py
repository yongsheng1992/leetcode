"""
    784. 字母大小写全排列
    -------------------
    回溯。
"""
from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []

        def solve(nums, temp):
            if not nums:
                res.append(temp)
                return

            char = nums[0]
            if char.isalpha():
                solve(nums[1:], temp + char.lower())
                solve(nums[1:], temp + char.upper())
            else:
                solve(nums[1:], temp + char)

        solve(S, "")
        return res
