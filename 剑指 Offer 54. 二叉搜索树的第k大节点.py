"""
    剑指 Offer 54. 二叉搜索树的第k大节点
    ---------------------------------
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res = []

        def solve(node):
            if not node:
                return False

            flag = solve(node.right)
            if flag:
                return True
            res.append(node.val)
            if len(res) == k:
                return True
            flag = solve(node.left)
            if flag:
                return True

        solve(root)
        return res[-1]
