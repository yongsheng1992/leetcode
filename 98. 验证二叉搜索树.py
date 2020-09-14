"""
    98. 验证二叉搜索树
    -----------------
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def in_order(node: TreeNode, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            if node.val >= upper or node.val <= lower:
                return False

            if not in_order(node.left, lower, node.val):
                return False

            if not in_order(node.right, node.val, upper):
                return False

            return True

        ans = in_order(root)
        return ans
