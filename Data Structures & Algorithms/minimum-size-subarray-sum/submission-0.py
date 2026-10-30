class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        m = 0
        l, r = 0, 0
        s = 0
        while r < len(nums):
            s += nums[r]
            while s >= target:
                if not m:
                    m = r - l + 1
                else:
                    m = min(r - l + 1, m)
                s -= nums[l]
                l += 1
            r += 1
        return m