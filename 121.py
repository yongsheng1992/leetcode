"""
    121. 买卖股票的最佳时机
    ---------------------
    遍历可能获取的所有可能，取出最大值。
    也可以使用动态规划：f[i]表示当前天获取的利润
    状态转移方程：f[i] = max(prices[i] - prices[i-1], f[i-1] + prices[i] - prices[i-1])
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        acc = 0
        for i in range(1, n):
            p = prices[i] - prices[i-1]

            if acc == 0 and p > 0:
                acc = p
                profit = max(acc, profit)
            elif acc + p > 0:
                acc += p
                profit = max(acc, profit)
            else:
                acc = 0

        return profit

    def dp(self, prices: List[int]):
        n = len(prices)
        if n == 0:
            return 0
        # f[i]表示当前天获取的利润
        # f[i] = max(prices[i] - prices[i-1], f[i-1] + prices[i] - prices[i-1])
        f = [0] * n

        for i in range(1, n):
            p = prices[i] - prices[i-1]
            f[i] = max(p, f[i-1] + p)

        return max(f)
