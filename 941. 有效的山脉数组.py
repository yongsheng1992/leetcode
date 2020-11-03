"""
    941. 有效的山脉数组
    ------------------
"""
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        i = 0
        for i in range(1, n):
            if A[i] < A[i-1]:
                break

            if A[i] == A[i-1]:
                return False

        i -= 1
        if i == 0:
            return False

        if i == n-1:
            return False

        for j in range(i+1, n):
            if A[j] >= A[j-1]:
                return False

        return True

