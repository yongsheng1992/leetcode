"""
    40. 组合总和 II
    --------------
    先排序，然后在递归
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        nums = sorted(candidates)

        def solve(nums, target, temp):
            if target == 0:
                res.append(temp)

            flag = set()
            for i, num in enumerate(nums):
                if target - num >= 0 and num not in flag:
                    flag.add(num)
                    flag.add(target - num)
                    solve(nums[i + 1:], target - num, temp + [num])

        solve(nums, target, [])
        return res
