class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {}
        for i, ch in enumerate(order):
            index[ch] = i

        for i in range(len(words) - 1):
            l1, l2 = 0, 0
            while l1 < len(words[i]) - 1 and l2 < len(words[i + 1]) - 1 and words[i][l1] == words[i + 1][l2]:
                l1 += 1
                l2 += 1

            if index[words[i][l1]] > index[words[i + 1][l2]]:
                return False
            if index[words[i][l1]] == index[words[i + 1][l2]] and len(words[i]) > len(words[i + 1]):
                return False

        return True
            
