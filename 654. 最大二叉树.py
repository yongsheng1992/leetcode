"""
    654. 最大二叉树
    --------------
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        def build(array):
            if not array:
                return None

            max_value = -1
            max_index = -1

            for i in range(len(array)):
                if array[i] > max_value:
                    max_value = array[i]
                    max_index = i

            node = TreeNode(max_value)
            node.left = build(array[0:max_index])
            node.right = build(array[max_index + 1:])

            return node

        return build(nums)
