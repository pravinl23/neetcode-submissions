class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i, path):
            if len(path) == k:
                res.append(path[:])
                return
            if (n - i + 1) < k - len(path):
                return
            
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

            backtrack(i + 1, path)

        backtrack(1, [])
        return res

            