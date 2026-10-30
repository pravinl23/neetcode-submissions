class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        count = 0
        while l <= r:
            while nums[l] == val:
                nums[l] = nums[r]
                nums[r] = "_"
                r -= 1
            l += 1

        return len(nums) - nums.count("_")