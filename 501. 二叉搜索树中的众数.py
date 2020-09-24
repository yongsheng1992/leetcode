"""
    501. 二叉搜索树中的众数
    --------------------
    根据二叉搜索说有序的性质
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        temp = []
        res = []
        max_count = 0

        def solve(node):
            if not node:
                return

            solve(node.left)
            temp.append(node.val)
            solve(node.right)

        solve(root)
        n = len(temp)

        if n == 0:
            return []

        res = []
        count = 1
        for i in range(1, n):
            if temp[i - 1] == temp[i]:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                    res.clear()
                    res.append(temp[i - 1])
                elif count == max_count:
                    res.append(temp[i - 1])
                count = 1

        if count > max_count:
            res.clear()
            res.append(temp[-1])
        elif count == max_count:
            res.append(temp[-1])

        return res
