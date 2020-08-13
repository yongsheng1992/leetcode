"""
    43. 字符串相乘
    -------------
    模拟简单的竖乘法即可。当然如果会其它的算法是加分项。比如分治乘法，快速傅里叶变换
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        prev = ''
        for index, b in enumerate(reversed(num2)):
            c = 0
            if index == 0:
                t = ''
            else:
                t = '0' * index

            for a in reversed(num1):
                m = int(a) * int(b)
                m += c

                c = m // 10
                r = m % 10
                t = str(r) + t

            if c != 0:
                t = str(c) + t

            if prev:
                n1 = len(prev)
                n2 = len(t)
                i, j = n1-1, n2 - 1
                temp = ''
                c = 0
                while i >= 0:
                    s = int(prev[i]) + int(t[j]) + c

                    c = s // 10
                    r = s % 10
                    temp = str(r) + temp
                    i -= 1
                    j -= 1

                while j >= 0:
                    s = int(t[j]) + c
                    c = s // 10
                    r = s % 10
                    temp = str(r) + temp
                    j -= 1

                if c != 0:
                    temp = str(c) + temp
                prev = temp

            else:
                prev = t

        if prev[0] == '0':
            i = 0
            for i in range(1, len(prev)):
                if prev[i] != '0':
                    break
            prev = prev.replace(prev[0:i], '')
            if prev == '':
                prev = '0'

        return prev
