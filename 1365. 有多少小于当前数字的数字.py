"""
    1365. 有多少小于当前数字的数字
    ---------------------------
    排序加上二分查找
"""
import bisect
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        res = [bisect.bisect_left(sorted_nums, num) for num in nums]

        return res
