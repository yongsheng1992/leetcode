"""
    面试题 04.03. 特定深度节点链表
    ----------------------------
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if not tree:
            return []
        queue = [tree]
        res = []

        while queue:

            dummy = ListNode(-1)
            list_node = dummy
            _queue = []
            while queue:
                node = queue.pop(0)
                list_node.next = ListNode(node.val)
                list_node = list_node.next
                _queue.append(node)

            for node in _queue:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(dummy.next)

        return res
