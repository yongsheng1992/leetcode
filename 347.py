"""
    347. 前 K 个高频元素
    -------------------
    维护一个大小为k的堆。Python可以直接使用heapq这个库，但是需要会手撸堆的实现。
"""
import heapq
from typing import List
from collections import Counter


class Pair:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.y < other.y

    def __gt__(self, other):
        return self.y > other.y

    def __eq__(self, other):
        return self.y == other.y


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        total = 0
        for key, cnt in counter.items():
            total += 1
            pair = Pair(key, cnt)
            if total <= k:
                heapq.heappush(heap, pair)
            else:
                heapq.heappushpop(heap, pair)

        return [pair.x for pair in heap]
