class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []

        def backtracking(path, index):
            if index == len(nums):
                return
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return

            path.append(nums[index])
            backtracking(path, index)
            path.pop()

            backtracking(path, index + 1)

        backtracking([], 0)
        return res