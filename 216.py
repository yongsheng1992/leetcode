"""
    216. 组合总和 III
    ----------------
    从大到下递归，减少递归的次数
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        nums = [i for i in range(9, 0, -1)]

        def solve(nums, cnt, target, temp):
            if target == 0 and cnt == 0:
                res.append(temp)

            if cnt == 0:
                return

            for i, num in enumerate(nums):
                if target - num * cnt > 0:
                    break

                if target - num >= 0:
                    solve(nums[i+1:], cnt-1, target-num, temp + [num])

        solve(nums, k, n, [])
        return res
