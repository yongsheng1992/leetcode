"""
    637. 二叉树的层平均值
    -------------------
    bfs遍历二叉树
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []

        queue = [(root, 0)]
        heights = {}
        sums = {}
        height = 0

        while queue:
            node, height = queue.pop(0)
            heights.setdefault(height, 0)
            sums.setdefault(height, 0)
            heights[height] += 1
            sums[height] += node.val

            if node.left:
                queue.append((node.left, height + 1))
            if node.right:
                queue.append((node.right, height + 1))

        res = []
        for i in range(height+1):
            res.append(sums[i]/heights[i])

        return res
