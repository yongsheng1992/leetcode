"""
    113. 路径总和 II
    ---------------
    回溯解决
"""
from typing import List
from copy import deepcopy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []

        def solve(node: TreeNode, acc, temp):
            if not node:
                return

            acc += node.val
            temp.append(node.val)
            if not node.left and not node.right:
                if acc == sum:
                    res.append(deepcopy(temp))
                temp.pop()
                return
            solve(node.left, acc, temp)
            solve(node.right, acc, temp)
            temp.pop()

        solve(root, 0, [])

        return res
