"""
    738. 单调递增的数字
    ------------------
"""
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N < 10:
            return 0 if N == 0 else N - 1

        str_n = str(N)
        temp = [i for i in str_n]
        for i in range(len(temp)-2, -1, -1):
            if temp[i] > temp[i+1]:
                temp[i] = str(int(temp[i]) - 1)
                for j in range(i+1, len(temp)):
                    temp[j] = '9'

        return int("".join(temp))
