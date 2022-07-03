class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        length = len(nums)
        i = length - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i < 0:
            return -1

        j = length - 1
        while j >=0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]
        ans = int("".join(nums))

        return ans if ans < 2 ** 31 else -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.nextGreaterElement(2147483486))
    print(solution.nextGreaterElement(12))
