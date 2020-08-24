"""
    459. 重复的子字符串
    -----------------
    暴力模拟。字串只可能是1到字符串长度的一半。然后将字符串分段比较。
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        mid = n // 2
        for i in range(1, mid+1):
            if n % i != 0:
                continue
            flag = True
            a = 0
            b = i
            while a + b + b <= n:
                if s[a:a+b] != s[a+b:a+b+b]:
                    flag = False
                    break
                a += b

            if flag:
                return flag

        return False
