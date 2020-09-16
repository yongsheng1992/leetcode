"""
    剑指 Offer 32 - II. 从上到下打印二叉树 II
    ---------------------------------------
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [root]

        while queue:

            _queue = []
            temp = []
            while queue:
                node = queue.pop(0)
                _queue.append(node)
                temp.append(node.val)

            for node in _queue:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(temp)

        return res
