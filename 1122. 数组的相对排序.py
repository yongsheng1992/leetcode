"""
    1122. 数组的相对排序
    -------------------
"""
from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        diff = set(arr1).difference(set(arr2))
        counter = Counter(arr1)
        res = []

        for item in arr2:
            for _ in range(counter[item]):
                res.append(item)

        for item in sorted(list(diff)):
            for _ in range(counter[item]):
                res.append(item)
        return res
