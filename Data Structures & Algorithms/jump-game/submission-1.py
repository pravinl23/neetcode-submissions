class Solution:
    def canJump(self, nums: List[int]) -> bool:

        nextValid = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= nextValid - i:
                nextValid = i


        return nextValid == 0