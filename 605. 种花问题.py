"""
    605. 种花问题
    ------------
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        length = len(flowerbed)
        flowerbed.append(0)

        if flowerbed[0] == 0 and flowerbed[1] != 1:
            flowerbed[0] = 1
            n -= 1

        for i in range(1, length):
            if n == 0:
                return True
            if flowerbed[i] == 1:
                continue

            if flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                n -= 1
                flowerbed[i] = 1

        return n == 0
