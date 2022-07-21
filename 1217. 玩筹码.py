from typing import List
from collections import Counter


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        counter = Counter(position)
        ans = 100000
        for key1 in counter.keys():
            temp = 0
            for key2, value2 in counter.items():
                if key2 == key1:
                    continue
                if abs(key2 - key1) % 2 != 0:
                    temp += value2
            ans = min(ans, temp)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minCostToMoveChips([2, 2, 2, 3, 3]))
    print(solution.minCostToMoveChips(position=[1, 2, 3]))
    print(solution.minCostToMoveChips(position=[1, 1000000000]))
    print(solution.minCostToMoveChips(position=[6,4,7,8,2,10,2,7,9,7]))
