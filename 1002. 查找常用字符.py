"""
    1002. 查找常用字符
    -----------------
"""
from typing import List
from collections import Counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        counters = {}
        flags = {}
        n = len(A)

        for string in A:
            counter = Counter(string)
            for k in set(string):
                flags.setdefault(k, 0)
                flags[k] += 1

            for k, v in counter.items():
                counters.setdefault(k, v)
                if v < counters[k]:
                    counters[k] = v

        ans = []
        for k, v in flags.items():
            if v == n:
                for _ in range(counters[k]):
                    ans.append(k)

        return ans
