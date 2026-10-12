class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates) - 1
        candidates.sort()

        def backtracking(path, index, currSum):
            if currSum == target:
                res.append(path[:])
                return
            if index > n or currSum > target:
                return

            path.append(candidates[index])
            backtracking(path, index + 1, currSum + candidates[index])
            path.pop()


            while index < n and candidates[index] == candidates[index + 1]:
                index += 1
            backtracking(path, index + 1, currSum)


        backtracking([], 0, 0)
        return res