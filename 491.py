"""
    491. 递增子序列
    --------------
    递归遍历所有可能的子序列，注意去重。
"""
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, temp):
            if len(temp) > 1:
                res.append(temp)

            flag = {}
            for i in range(len(nums)):
                if nums[i] in flag:
                    continue
                if not temp or nums[i] >= temp[-1]:
                    flag[nums[i]] = 1
                    dfs(nums[i+1:], temp+[nums[i]])

        dfs(nums, [])
        return res
