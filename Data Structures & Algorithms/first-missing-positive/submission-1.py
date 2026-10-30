class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m = max(nums)
        nums = set(nums)
        for i in range(1, m):
            if i not in nums:
                return i

        if m < 0:
            return 1
        return m + 1