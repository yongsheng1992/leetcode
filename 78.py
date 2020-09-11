"""
    78. 子集
    -------
    简单的递归
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def solve(nums, temp):
            res.append(temp)

            for i, num in enumerate(nums):
                solve(nums[i+1:], temp + [num])

        solve(nums, [])

        return res
