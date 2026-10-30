class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        res, runningSum = 0, 0
        for i in range(len(nums)):
            runningSum += nums[i]
            res += count[runningSum - k]
            count[runningSum] += 1

        return res
