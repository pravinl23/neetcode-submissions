class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = []
        nums.sort()


        def backtracking(path, index):
            res.append(path[:])
            for i in range(index, n):
                if i > index and nums[i] == nums[i - 1]:
                    continue 
                path.append(nums[i])
                backtracking(path, i + 1)
                path.pop()


        backtracking([], 0)

        return res

