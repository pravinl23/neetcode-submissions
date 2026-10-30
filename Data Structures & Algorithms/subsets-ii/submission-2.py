class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        def backtrack(path, i):
            print(path)
            if i == n:
                res.append(path[:])
                return

            # include
            path.append(nums[i])
            backtrack(path, i + 1)
            path.pop()
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            # exclude
            backtrack(path, i + 1)

        backtrack([], 0)
        return res