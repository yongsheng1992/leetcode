"""
    57. 插入区间
    -----------
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        x, y = newInterval
        left = []
        right = []

        for a, b in intervals:
            if b < x:
                left.append([a, b])

            if a > y:
                right.append([a, b])

            if a <= x <= b:
                x = a

            if a <= y <= b:
                y = b

        return left + [[x, y]] + right
