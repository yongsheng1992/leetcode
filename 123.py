"""
    123. 买卖股票的最佳时机 III
    --------------------------
    看题解做出来的。计算第一次买和第两次买的最小价格，然后在计算第一次卖和第二次卖的最大价格。即使是k次交易，也可以这样依次类推。
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 0:
            return 0

        one_cost, one_profit = 2147483647, 0
        two_cost, two_profit = 2147483647, 0

        for price in prices:
            one_cost = min(price, one_cost)
            one_profit = max(one_profit, price - one_cost)
            two_cost = min(two_cost, price - one_profit)
            two_profit = max(two_profit, price - two_cost)

        return two_profit
