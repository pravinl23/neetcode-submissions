class Node:
    def __init__(self, val, key):
        self.val = val
        self.prev = None
        self.next = None
        self.key = key

    def delete(self):
        tempnext = self.next
        tempprev = self.prev
        if tempnext:
            tempprev.next = tempnext
        if tempprev:
            tempnext.prev = tempprev
    def add(self, first, third):
        self.prev = first
        self.next = third
        first.next = self
        if third:
            third.prev = self

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key : node
        back = Node("back", "back")
        front = Node("front", "back")
        back.add(front, None)
        self.back = back
        self.front = front


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        n = self.cache[key]
        n.delete()
        n.add(self.front, self.front.next)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
        else:
            self.cache[key] = Node(value, key)
            self.capacity -= 1
        
        n = self.cache[key]
        n.delete()
        n.add(self.front, self.front.next)

        if self.capacity < 0:
            self.capacity += 1
            n = self.back.prev
            n.delete()
            del self.cache[n.key]
        
