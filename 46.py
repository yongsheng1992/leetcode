"""
    46. 全排列
    ---------
    递归
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def solve(nums, temp):
            if not nums:
                res.append(temp)

            for i, num in enumerate(nums):
                solve(nums[:i] + nums[i+1:], temp + [num])

        solve(nums, [])
        return res
