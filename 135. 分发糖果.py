"""
    135. 分发糖果
    -------------
"""
from typing import List
from collections import OrderedDict


class Solution:
    def candy(self, ratings: List[int]) -> int:
        mapping = {}
        n = len(ratings)

        if n <= 1:
            return n

        res = [1] * n
        for idx, value in enumerate(ratings):
            mapping.setdefault(value, [])
            mapping[value].append(idx)

        for i, value in sorted(mapping.items(), key=lambda x: x[0]):
            for j in value:
                if ratings[j] != i:
                    continue

                if j - 1 >= 0 and ratings[j] > ratings[j-1]:
                    res[j] = max(res[j], res[j-1] + 1)

                if j + 1 < n and ratings[j] > ratings[j+1]:
                    res[j] = max(res[j], res[j+1] + 1)

        return sum(res)
