import math
import asyncio

class Solution:
    MOD = 1000000007

    def __init__(self):
        self.cache = [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 17, 17, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25]

    def numPrimeArrangements(self, n: int) -> int:
        prime_num = self.cache[n]
        remain = n - self.cache[n]
        return (math.factorial(prime_num) % self.MOD ) * (math.factorial(remain) % self.MOD) % self.MOD


if __name__ == "__main__":
    solution = Solution()
    print(solution.numPrimeArrangements(5))
    print(solution.numPrimeArrangements(100))
