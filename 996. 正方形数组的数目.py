"""
    996. 正方形数组的数目
    -------------------
    全排列的加强版，在计算全排列的时候剪枝。
"""
import math
from typing import List


class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:

        res = 0


        def permutation(array, temp):
            if not array:
                nonlocal res
                res += 1

            flag = set()
            for i in range(len(array)):
                num = array[i]
                if num not in flag:
                    if len(temp) > 0:
                        a = int(math.sqrt(temp[-1] + num))
                        if a * a == (temp[-1] + num):
                            flag.add(num)
                            permutation(array[0:i] + array[i + 1:], temp + [num])
                    elif len(temp) == 0:
                        flag.add(num)
                        permutation(array[0:i] + array[i + 1:], temp + [num])
        permutation(A, [])
        return res
