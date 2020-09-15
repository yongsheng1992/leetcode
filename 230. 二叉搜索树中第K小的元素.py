"""
    230. 二叉搜索树中第K小的元素
    --------------------------
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        stop = False

        def dfs(root):
            nonlocal stop
            if not root or stop:
                return

            dfs(root.left)
            if len(res) == k:
                stop = True
                return
            res.append(root.val)
            dfs(root.right)

        dfs(root)

        return res[-1]
