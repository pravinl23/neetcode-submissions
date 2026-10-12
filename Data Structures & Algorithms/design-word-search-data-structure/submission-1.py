class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        t = self.trie
        for char in word:
            if char not in t:
                t[char] = {}
            t = t[char]
        t["#"] = True


    def recurseSearch(self, word, i, t):
        if i == len(word):
            return "#" in t

        if word[i] == ".":
            for subt in t:
                if subt != "#":
                    if self.recurseSearch(word, i + 1, t[subt]):
                        return True
            return False
        
        if word[i] not in t:
            return False
        return self.recurseSearch(word, i + 1, t[word[i]])
        
    def search(self, word: str) -> bool:
        return self.recurseSearch(word, 0, self.trie)