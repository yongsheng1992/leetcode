"""
    547. 省份数量
    ------------
"""
from typing import List

class UF:

    def __init__(self, n):
        self._ids = [0] * n
        self._n = n
        self._count = n

        for i in range(0, n):
            self._ids[i] = i

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)

        if p_id == q_id:
            return

        for i in range(0, self._n):
            if self._ids[i] == p_id:
                self._ids[i] = q_id

        self._count -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        return self._ids[p]

    def count(self):
        return self._count


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        if n <= 1:
            return n

        uf = UF(len(isConnected))

        for i in range(0, len(isConnected)):
            for j in range(i+1, len(isConnected[0])):
                if isConnected[i][j]:
                    uf.union(i, j)

        return uf.count()


if __name__ == '__main__':
    solution = Solution()
    print(solution.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))