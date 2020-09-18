"""
    897. 递增顺序查找树
    -----------------
    递归练习
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def in_order(node: TreeNode, new_node: TreeNode):

            if not node:
                return new_node

            new_node = in_order(node.left, new_node)
            new_node.right = TreeNode(node.val)
            new_node = new_node.right
            new_node = in_order(node.right, new_node)

            return new_node

        dummy = TreeNode(0)
        in_order(root, dummy)
        return dummy.right
