class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        visiting = set()
        def backtrack(path):
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                if nums[i] in visiting:
                    continue
                visiting.add(nums[i])
                path.append(nums[i])
                backtrack(path)
                path.pop()
                visiting.remove(nums[i])

        backtrack([])
        return res