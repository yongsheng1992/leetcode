"""
    226. 翻转二叉树
    -------------
    一遍中序遍历，一遍创建新的树
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node: TreeNode):
            if not node:
                return None

            new_node = TreeNode(node.val)
            new_node.right = dfs(node.left)
            new_node.left = dfs(node.right)
            return new_node

        return dfs(root)
