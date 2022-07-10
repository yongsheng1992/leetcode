from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        length = len(arr)
        min_abs = 2147483647
        if length == 2:
            return [[arr[0], arr[1]]]

        res = []
        for i in range(length-1):
            d = arr[i+1] - arr[i]
            if d < min_abs:
                min_abs = d
                res = []
            if d == min_abs:
                res.append([arr[i], arr[i+1]])

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))
    print(solution.minimumAbsDifference([1,3,6,10,15]))
    print(solution.minimumAbsDifference([4,2,1,3]))