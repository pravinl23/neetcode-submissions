class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["done"] = True


    def search(self, word: str) -> bool:
        n = len(word)
        done = False
        def dfs(i, root):
            nonlocal done
            if i == n:
                if "done" in root:
                    done = True
                return
            
            if word[i] == ".":
                for next_root in root:
                    if next_root != "done":
                        dfs(i + 1, root[next_root])
            elif word[i] in root:
                dfs(i + 1, root[word[i]])

            
        dfs(0, self.trie)
        return done



