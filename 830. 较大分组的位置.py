"""
    830. 较大分组的位置
    ------------------
"""
from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        n = len(s)
        res = []

        start, end = 0, 0
        for i in range(1, n):
            if s[i] != s[i-1]:
                if end - start >= 2:
                    res.append([start, end])
                start, end = i, i
            else:
                end = i
        if start != end and end - start >= 2:
            res.append([start, end])
        return res