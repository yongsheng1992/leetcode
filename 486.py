"""
    486. 预测赢家
    ------------
    如果使用动态规划，f[i][j]便是i到j的最大分数差。
    f[i][i] = nums[i]
    f[i][j] = max(num[i]-f[i+1][j],num[j]-f[i][j-1])
"""
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def solve(start, end, turn):
            if start == end:
                return nums[start] * turn

            res1 = nums[start] * turn + solve(start+1, end, -turn)
            res2 = nums[end] * turn + solve(start, end-1, -turn)

            return max(res1 * turn, res2 * turn) * turn
        res = solve(0, len(nums)-1, 1)
        return res >= 0

    def dp(self, nums):
        n = len(nums)
        f = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n-1, -1, -1):
            f[i][i] = nums[i]
            for j in range(i+1, n):
                f[i][j] = max(nums[i]-f[i+1][j], nums[j]-f[i][j-1])

        return f[0][-1] >= 0
