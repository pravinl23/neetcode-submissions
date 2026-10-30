class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        m = float('inf')
        l, r = 0, 0
        s = 0
        while r < len(nums):
            s += nums[r]
            while s >= target:
                m = min(r - l + 1, m)
                s -= nums[l]
                l += 1
            r += 1
        if m == float('inf'):
            return 0
        return m