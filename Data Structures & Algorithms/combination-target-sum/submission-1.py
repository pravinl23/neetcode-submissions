class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []
        def backtrack(i, s):
            if i == len(nums):
                return
            if s == target:
                res.append(curr[:])
                return
            if s > target:
                return

            curr.append(nums[i])
            backtrack(i, s + nums[i])
            curr.pop()

            backtrack(i + 1, s)

        backtrack(0, 0)

        return res