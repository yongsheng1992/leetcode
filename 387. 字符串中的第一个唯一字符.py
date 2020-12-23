"""
    387. 字符串中的第一个唯一字符
    --------------------------
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for idx, char in enumerate(s):
            counter.setdefault(char, [])
            counter[char].append(idx)

        res = 999999999
        for key, value in counter.items():
            if len(value) == 1:
                res = min(value[0], res)

        return res if res != 999999999 else -1
