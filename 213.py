"""
    213. 打家劫舍 II
    ---------------
    在198. 打家劫舍中，房间不是首尾相连的，本题中的房间是首位相连的。也就是说最后一个房间抢还是不抢，取决与第一个房间。
    如果第一个房间被抢了，直接不需要考虑最后一个房间。
    如果第一个房间没有被抢，可以考虑最后一个房间。
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2 or len(nums) == 3:
            return max(nums)

        a, b, n = nums[0], 0, len(nums)
        return max(a + self.rob1(nums[2:-1]), self.rob1(nums[1:]))

    def rob1(self, nums):
        a, b = 0, 0

        for num in nums:
            a, b = b + num, max(a, b)

        return max(a, b)
