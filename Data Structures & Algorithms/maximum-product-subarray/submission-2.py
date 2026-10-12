class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max, min
        m = nums[0]
        nums[0] = [nums[0], nums[0]]
        for i in range(1, len(nums)):
            n1 = nums[i] * nums[i - 1][0]
            n2 = nums[i] * nums[i - 1][1]
            nums[i] = [max(n1, n2, nums[i]), min(n1, n2, nums[i])]
            m = max(m, nums[i][0], nums[i][1])
        return m