class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        adjacencyList = {}
        for w in wordList:
            adjacencyList[w] = []
        chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        setWordList = set(wordList)
        for w in wordList:
            for i, ch in enumerate(w):
                for replacement in chars:
                    if ch == replacement:
                        continue
                    wlist = list(w)
                    wlist[i] = replacement
                    tempword = "".join(wlist)
                    if tempword in setWordList:
                        adjacencyList[w].append(tempword)

        queue = deque()
        queue.append([beginWord, 1])
        done = set()
        while queue:
            w, c = queue.popleft()
            if w == endWord:
                return c

            done.add(w)
            for nei in adjacencyList[w]:
                if nei in done:
                    continue
                queue.append([nei, c + 1])

        return 0
            