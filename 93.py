from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        nums = [int(i) for i in s]
        n = len(nums)
        for i in range(3):
            if self.solve(i, nums, 1, n):
               print(i)

    def solve(self, i, nums, cnt, n):
        if cnt == 4:
            return self.valid(nums[i:])

        res = False
        for j in range(i+1, min(i+3, n)):
            print(i, cnt)
            if self.valid(nums[i:j]):
                res |= self.solve(i, nums[i:j], cnt+1, n)

        return res

    @staticmethod
    def valid(nums):
        if len(nums) > 1 and nums[0] == 0:
            return False
        value = 0
        for num in nums:
            value *= 10
            value += num

        if 0 <= value <= 255:
            return True

        return False


if __name__ == '__main__':
    s = "9999999"
    solution = Solution()
    nums = [int(i) for i in s]
    print(solution.restoreIpAddresses(s))