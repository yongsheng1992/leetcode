"""
    215. 数组中的第K个最大元素
    ------------------------
"""
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        cnt = 0
        for num in nums:
            cnt += 1
            if cnt <= k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)

        return heapq.heappop(heap)
