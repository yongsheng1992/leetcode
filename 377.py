"""
    377. 组合总和 Ⅳ
    ---------------
    动态规划
"""
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        f = [0] * (target + 1)
        f[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    f[i] += f[i-num]

        return f[target]
