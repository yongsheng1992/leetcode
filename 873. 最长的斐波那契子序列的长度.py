from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        length = len(arr)
        cache = {num: idx for idx, num in enumerate(arr)}
        dp = [[0 for _ in range(length)] for _ in range(length)]
        ans = 0
        for i in range(length):
            for j in range(i+1, length):
                num = arr[j] - arr[i]
                if num in cache:
                    h = cache[num]
                    if h < i:
                        dp[i][j] = max(dp[h][i] + 1, 3)
                        ans = max(ans, dp[i][j])
        return ans

    def solve(self, x, y, arr) -> int:
        ans = 0
        for idx, num in enumerate(arr):
            if x + y == num:
                temp = self.solve(y, num, arr[idx + 1:]) + 1
                ans = max(ans, temp)
        return ans

    def solve1(self, arr):
        length = len(arr)
        cache = {num: idx for idx, num in enumerate(arr)}
        dp = [[0 for _ in range(length)] for _ in range(length)]
        ans = 0
        for i in range(length):
            for j in range(i+1, length):
                num = arr[j] - arr[i]
                if num in cache:
                    h = cache[num]
                    if h < i:
                        dp[i][j] = max(dp[h][i] + 1, 3)
                        ans = max(ans, dp[i][j])

        return ans
if __name__ == "__main__":
    solution = Solution()
    print(solution.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
    # print(solution.lenLongestFibSubseq([1,3,7,11,12,14,18]))
    print(solution.lenLongestFibSubseq([2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]))
    print(solution.lenLongestFibSubseq([1,3,5]))
    print(solution.solve1([1,2,3,4,5,6,7,8]))
    print(solution.solve1([2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]))
