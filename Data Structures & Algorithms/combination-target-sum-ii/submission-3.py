class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(path, s, i):
            if s == target:
                res.append(path[:])
                return

            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if s + candidates[j] > target:
                    break
                path.append(candidates[j])
                backtrack(path, s + candidates[j], j + 1)
                path.pop()

        backtrack([], 0, 0)
        return res