"""
    538. 把二叉搜索树转换为累加树
    --------------------------
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        def solve(node: TreeNode, acc):
            if not node:
                return acc

            acc = solve(node.right, acc)
            acc += node.val
            node.val = acc
            acc = solve(node.left, acc)

            return acc

        solve(root, 0)

        return root
