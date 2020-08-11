"""
    99. 恢复二叉搜索树
    ----------------
    题目中规定了只有两个节点被交换了了位置。那么如何找到这两个节点呢？
    首先使用中序遍历可以得到有序的列表，假设得到[a1, a2, ... , an]。
    两个节点交互有两种情况，相邻的两个节点交换，和不相邻的两个节点交换。
    这两种交换对整个列表的有序性破环不一样：
    1. 相邻交换，遍历列表的时候，只能找到一个节点破坏了有序性
    2. 不相邻交换，有两个节点破坏了有序性
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        order = []
        self.in_order(root, order)
        n = len(order)
        res = []
        for i in range(0, n-1):
            if order[i].val > order[i+1].val:
                res.append(i)

        if len(res) == 1:
            a, b = order[res[0]], order[res[0]+1]
            a.val, b.val = b.val, a.val
        elif len(res) == 2:
            a, b = order[res[0]], order[res[1]+1]
            a.val, b.val = b.val, a.val

    def in_order(self, root, order):
        if not root:
            return

        self.in_order(root.left, order)
        order.append(root)
        self.in_order(root.right, order)
