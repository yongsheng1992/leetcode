"""
    783. 二叉搜索树节点最小距离
    ------------------------
    当前节点需要和左子树的最大值比较，和右子树的最小值比较。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def solve(node: TreeNode):
            if not node:
                return float('inf'), float('-inf'), float('inf')

            a, b, c = solve(node.left)
            d, e, f = solve(node.right)

            return min(a, node.val), max(e, node.val), min(c, f, abs(node.val - b), abs(d - node.val))

        _, _, ans = solve(root)
        return ans
