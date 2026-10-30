class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        seen = set()
        def backtrack(i, path):
            if i == len(nums):
                res.append(path[:])
                return
            
            for j in range(len(nums)):
                if j in seen:
                    continue
                if j < len(nums) - 1 and nums[j] == nums[j + 1] and j + 1 not in seen:
                    continue
                
                path.append(nums[j])
                seen.add(j)
                backtrack(i + 1, path)
                path.pop()
                seen.remove(j)
            
            return

        backtrack(0, [])
        return res