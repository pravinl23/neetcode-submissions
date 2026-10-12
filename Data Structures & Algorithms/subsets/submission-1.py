class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(path, i):
            if i == len(nums):
                res.append(path[:])
                return
            # case 1: include
            path.append(nums[i])
            backtrack(path, i + 1)
            path.pop()

            # case 2: exclude
            backtrack(path, i + 1)

        backtrack([], 0)
        return res