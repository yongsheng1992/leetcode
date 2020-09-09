"""
    47. 全排列 II
    ------------
    迭代的时候，取消重复元素的迭代
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def solve(nums, temp):
            if not nums:
                res.append(temp)

            flag = set()
            for i, num in enumerate(nums):
                if num not in flag:
                    flag.add(num)
                    solve(nums[0:i] + nums[i + 1:], temp + [num])

        solve(nums, [])

        return res
