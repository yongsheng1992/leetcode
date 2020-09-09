"""
    39. 组合总和
    -----------
    递归加减枝
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def solve(nums, remain, temp):
            if remain == 0:
                res.append(temp)
                return

            for i, num in enumerate(nums):
                j = 1
                while j * num <= remain:
                    solve(nums[i+1:], remain - num * j, temp + ([num] * j))
                    j += 1

        solve(candidates, target, [])

        return res
