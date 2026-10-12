class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["."] = True
        return

    def search(self, word: str) -> bool:
        curr = self.trie
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        if "." in curr and curr["."]:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True
        