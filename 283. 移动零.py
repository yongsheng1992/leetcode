"""
    283. 移动零
    ----------
"""
from typing import List
from heapq import heappop, heappush


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, n = 0, len(nums)
        q = []

        while i < n:
            if nums[i] == 0:
                q.append(i)
                i += 1
                continue

            if len(q) != 0:
                idx = heappop(q)
                nums[i], nums[idx] = nums[idx], nums[i]
                heappush(q, i)

            i += 1
