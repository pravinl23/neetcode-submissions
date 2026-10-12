class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        def backtracking(path, i):
            if i == len(nums):
                res.append(path[:])
                return

            # case 1 include:
            path.append(nums[i])
            backtracking(path, i + 1)
            path.pop()

            # skip duplicates 
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    i += 1
            # case 2: exclude:
            backtracking(path, i + 1)

        backtracking([], 0)

        return res
            