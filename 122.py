"""
    122. 买卖股票的最佳时机 II
    ------------------------
    只要遵循跌买涨卖即可。只要相邻两天的利润为整数，就是可以获取的。如果是负数，那么就不会买。
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        profit = 0

        for i in range(1, n):
            p = prices[i] - prices[i-1]

            if p > 0:
                profit += p

        return profit
