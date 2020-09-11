"""
    90. 子集 II
    -----------
    空间复杂度优化。
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        n = len(nums)

        def solve(idx, temp):
            res.append(temp)

            for i in range(idx, n):
                if i > idx and nums[i] == nums[i-1]:
                    continue

                solve(i+1, temp + [nums[i]])

        solve(0, [])
        return res
