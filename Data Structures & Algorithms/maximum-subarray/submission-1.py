class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        runningSum = 0
        m = -10000

        for n in nums:
            runningSum += n
            if n > runningSum:
                runningSum = n
            m = max(m, runningSum)


        return m
        