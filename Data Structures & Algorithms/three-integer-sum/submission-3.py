class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if not nums:
            return []
        res = []
        prev = None
        for i, target in enumerate(nums):
            if target == prev:
                continue
            else:
                l, r = i + 1, len(nums) - 1
                while l < r:
                    if nums[r] + nums[l] == -target:
                        res.append([target, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif nums[r] + nums[l] < -target:
                        l += 1
                    else:
                        r -= 1
            prev = target
        return res