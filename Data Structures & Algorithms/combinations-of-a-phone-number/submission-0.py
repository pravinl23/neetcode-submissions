class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        chars = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl",
                 "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}

        res = []
        def backtrack(path, i):
            if i == len(digits):
                res.append(path)
                return

            for ch in chars[digits[i]]:
                backtrack(path + ch, i + 1)

        backtrack("", 0)
            
        return res