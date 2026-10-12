class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        recent = [0]
        maxlen = max(len(w) for w in wordDict)

        for i in range(1, len(s) + 1):
            for j in range(len(recent) - 1, -1, -1):
                if i - recent[j] > maxlen:
                    break
                word = s[recent[j]:i]
                if word in wordDict:
                    recent.append(i)
                    break
            
        return recent[-1] == len(s)