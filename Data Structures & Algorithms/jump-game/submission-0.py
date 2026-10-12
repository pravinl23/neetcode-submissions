class Solution:
    def canJump(self, nums: List[int]) -> bool:

        res = True
        nextValid = None
        for i in range(len(nums) - 1, -1, -1):
            if not nextValid:
                nextValid = i
            elif nums[i] >= nextValid - i:
                nextValid = i


        return nextValid == 0