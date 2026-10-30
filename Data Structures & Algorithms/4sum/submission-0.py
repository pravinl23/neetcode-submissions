class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:            
        n = len(nums)
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                t = target - nums[i] - nums[j]
                l, r = j + 1, n - 1
                while l < r:
                    if nums[l] + nums[r] == t:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif nums[l] + nums[r] > t:
                        r -= 1
                    elif nums[l] + nums[r] < t:
                        l += 1

        return res
                