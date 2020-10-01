"""
    771. 宝石与石头
    --------------
"""
from collections import Counter


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = Counter(S)
        ans = 0

        for char in J:
            ans += counter.get(char, 0)

        return ans
