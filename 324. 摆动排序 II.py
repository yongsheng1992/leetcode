from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        sorted_nums = sorted(nums)
        mid = (n+1) // 2
        j, k = mid - 1, n - 1
        for i in range(0, n, 2):
            nums[i] = sorted_nums[j]
            if i + 1 < n:
                nums[i+1] = sorted_nums[k]
            j -= 1
            k -= 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.wiggleSort([1, 5, 1, 1, 6, 4]))
    print(solution.wiggleSort([1, 3, 2, 2, 3, 1]))
    print(solution.wiggleSort([1, 1, 2, 1, 2, 2, 1]))
    print(solution.wiggleSort([1]))
    print(solution.wiggleSort([1,4,3,4,1,2,1,3,1,3,2,3,3]))
    print(solution.wiggleSort([4,5,5,5,5,6,6,6]))
    print(solution.wiggleSort([5,8,5,7,3,6,2,5,1]))
