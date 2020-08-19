"""
    647. 回文子串
    ------------
    简单的动态规划，但是需要知道如何求解子问题。f[i][j]如果是回文串，取决与f[i+1][j-1]和s[i]是否与s[j]相等。
    然后处理边界问题。
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        f = [[0 for _ in range(n)] for _ in range(n)]
        ans = 0

        for i in range(n-1, -1, -1):
            f[i][i] = 1
            ans += 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if i + 1 > j - 1 or f[i+1][j-1]:
                        f[i][j] = 1
                        ans += 1

        return ans
