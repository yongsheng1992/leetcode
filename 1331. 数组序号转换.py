from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        mapping = dict()

        order = 0
        for num in sorted_arr:
            if num not in mapping:
                order += 1
            mapping.setdefault(num, order)

        return [mapping[num] for num in arr]