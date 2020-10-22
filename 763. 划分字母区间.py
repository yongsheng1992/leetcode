from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        n, i, j = len(S), 0, 0
        counters = {}
        res = []

        if n == 0:
            return res

        for i in range(n):
            counters.setdefault(S[i], [])
            counters[S[i]].append(i)
        
        cnt = 0
        i = 0
    
        while i < n:
            idx = counters[S[i]]
            s, e, j = idx[0] + 1, idx[-1], idx[0] + 1

            while j < e:
                e = max(counters[S[j]][-1], e)
                j += 1

            print(S[i], s, e, idx[-1])
            res.append(e - s + 2)
            i = e + 1

        return res
