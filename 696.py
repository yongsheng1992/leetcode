"""
    696. 计数二进制子串
    ------------------
    记录每次前后不一致的下标，然后对于每个下标，计算离它最近的下标的距离，距离之和就是答案。
    本题主要是需要处理边界，比如第一个和最后一个下标需要特殊处理。
"""

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        step, prev = 100000, 0

        for i in range(1, n):
            if s[i] != s[i-1]:
                if prev != 0:
                    ans += min(i - prev, step)
                step = i - prev
                prev = i

        if prev == 0:
            return 0
        ans += min(n-prev, step)
        return ans

