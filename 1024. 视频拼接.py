"""
    1024. 视频拼接
    -------------
    动态规划
"""
from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        f = [9999 for _ in range(T + 1)]
        f[0] = 0

        for t in range(1, T + 1):
            for x, y in clips:
                if x < t <= y:  # 如果t在x和y之间，那么至少需要裁剪该区间
                    f[t] = min(f[t], f[x] + 1)

        return -1 if f[T] == 9999 else f[T]
