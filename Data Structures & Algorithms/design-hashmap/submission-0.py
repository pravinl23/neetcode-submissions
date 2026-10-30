class MyHashMap:

    def __init__(self):
        self.l = []

    def put(self, key: int, value: int) -> None:
        for i, pair in enumerate(self.l):
            if pair[0] == key:
                self.l[i][1] = value
                return
        self.l.append([key, value])

    def get(self, key: int) -> int:
        for i, pair in enumerate(self.l):
            if pair[0] == key:
                return pair[1]

        return -1

    def remove(self, key: int) -> None:
        for i, pair in enumerate(self.l):
            if pair[0] == key:
                self.l.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)