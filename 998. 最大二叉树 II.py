"""
    998. 最大二叉树 II
    -----------------
    附加值对应的节点的插入位置是固定的。只能是它父节点的右子节点。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        def solve(node: TreeNode, parent: TreeNode, val: int):
            if not node:
                parent.right = TreeNode(val)
                return

            if node.val < val:
                parent.right = TreeNode(val)
                parent.right.left = node
                return

            solve(node.right, node, val)

        dummy = TreeNode(-1)
        dummy.right = root

        solve(root, dummy, val)

        return dummy.right
