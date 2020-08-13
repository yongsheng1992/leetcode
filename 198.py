"""
    198. 打家劫舍
    -------------
    对于当前房间，可以选择抢和不抢。但是相邻的房间不可以都被抢。
    最后一个房间的收益取决上一个放房间的收益，如果上一个房间被抢，那么当前房间不能被抢。所以需要有两个变量来保存上一个
    房间的收益（不抢和抢）。
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # a/b 抢/不抢
        a, b = 0, 0
        for num in nums:
            a, b = b + num, max(a, b)

        return max(a, b)
