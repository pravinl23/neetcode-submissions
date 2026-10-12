class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums 0 -> n add up to n(n - 1) // 2    harmonic series
        n = len(nums)
        expected = (n * (n + 1)) // 2
        return expected - sum(nums)