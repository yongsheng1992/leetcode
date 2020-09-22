"""
    968. 监控二叉树
    --------------
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:

        def solve(node: TreeNode):
            if not node:
                return [float('inf'), 0, 0]

            la, lb, lc = solve(node.left)
            ra, rb, rc = solve(node.right)
            a = lc + rc + 1
            b = min(a, la + rb, lb + ra)
            c = min(a, lb + rb)
            return a, b, c

        _, ans, _ = solve(root)

        return ans
