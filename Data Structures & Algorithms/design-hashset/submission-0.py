class MyHashSet:

    def __init__(self):
        self.l = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.l.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.l.remove(key)

    def contains(self, key: int) -> bool:
        for element in self.l:
            if element == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)