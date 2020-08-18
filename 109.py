"""
    109. 有序链表转换二叉搜索树
    -------------------------
    二叉搜索树的中序遍历的结果就是一个有序数组。对游戏链表的正序其实就是对二叉搜索树的中序遍历。
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        list_node = head
        while list_node:
            nums.append(list_node.val)
            list_node = list_node.next

        return self.insert(nums, 0, len(nums)-1)

    def insert(self, nums, l, r):
        if l > r:
            return None
        mid = (l + r) // 2
        node = TreeNode(nums[mid])
        if l <= mid - 1:
            node.left = self.insert(nums, l, mid-1)
        if r >= mid + 1:
            node.right = self.insert(nums, mid+1, r)
        return node
