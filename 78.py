"""
    78. 子集
    -------
    可以用递归，也可以用回溯
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res += [cur + [num] for cur in res]

        return res
