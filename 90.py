"""
    90. 子集 II
    -----------
    使用回溯，因为在每一步需要做去重。
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def solve(nums, temp):
            res.append(temp)

            flag = set()
            for i, num in enumerate(nums):
                if num not in flag:
                    flag.add(num)
                    solve(nums[i+1:], temp + [num])

        solve(sorted(nums), [])
        return res
