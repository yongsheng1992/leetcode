"""
    173. 二叉搜索树迭代器
    ------------------
    题目的提示只能使用O(h)的空间复杂度，可以联想到先将左节点全部放到栈中。
    然后每次抛出栈顶元素，然后此时处理有节点，及其所有子左节点。
    next方法无法是O(1)，但是不超过O(h)。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        node = root
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        val = node.val
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) != 0
