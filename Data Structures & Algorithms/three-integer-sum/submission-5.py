class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums) - 1
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1  
            r = n
            # num + nums[l] + nums[r] = 0
            while l < r:
                s = num + nums[l] + nums[r]
                if s == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
        return res