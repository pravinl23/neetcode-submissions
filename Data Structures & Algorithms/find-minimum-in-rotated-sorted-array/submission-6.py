class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums)
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            delta_l = nums[l] - nums[l - 1]
            delta_r = nums[r] - nums[r - 1]
            m = (l + r) // 2
            if delta_l < 0: 
                return nums[l]
            if delta_r < 0:
                return nums[r]
            
            if nums[l] < nums[m]:
                l = m + 1
            else:
                r = m
            