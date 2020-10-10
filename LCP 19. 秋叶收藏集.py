"""
    LCP 19. 秋叶收藏集
    -----------------
    动态规划
"""


class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        if n < 3:
            return 0

        f = [[100000 for _ in range(3)] for _ in range(n)]

        if leaves[0] == 'y':
            f[0][0] = 1
        else:
            f[0][0] = 0

        for i in range(1, n):
            if leaves[i] == 'y':
                f[i][0] = f[i-1][0] + 1
                f[i][1] = min(f[i-1][1], f[i-1][0])
                f[i][2] = min(f[i-1][2], f[i-1][1]) + 1
            else:
                f[i][0] = f[i-1][0]
                f[i][1] = min(f[i-1][1], f[i-1][0]) + 1
                f[i][2] = min(f[i-1][2], f[i-1][1])

        return f[n-1][2]
