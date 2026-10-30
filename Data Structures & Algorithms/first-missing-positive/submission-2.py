class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = 0.5

        for i in range(n):
            if abs(nums[i]) != 0.5 and abs(nums[i]) < n + 1:
                nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])

        for ans in range(1, n + 1):
            if nums[ans - 1] > 0:
                return ans
        return n + 1