class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        recent = [0]
        for i in range(1, len(s) + 1):
            for j in recent:
                word = s[j:i]
                if word in wordDict:
                    recent.append(i)
                    break
            
        if len(s) in recent:
            return True
        return False