"""
    77. 组合
    --------
    使用递归
"""
from typing import List
from copy import deepcopy


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        res = []

        def solve(nums, k, ans):
            if k == 0:
                res.append(ans)
                return

            for i, num in enumerate(nums):
                solve(nums[i+1:], k-1, ans + [num])

        solve(nums, k, [])

        return res
