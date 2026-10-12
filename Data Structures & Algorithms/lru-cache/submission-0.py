class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # {key : Node(key,val)}

        self.left = Node(None, None)
        self.right = Node(None, None) # temp vals, won't be stored in dict
        
        #pointing at each other to be doubly linked
        self.left.next = self.right #[Left]->[Right]
        self.right.prev = self.left #[Left]<-> [Right]

        
    # HELPER FUNCTIONS
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        # put at the end
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt


        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) # remove from where it is
            self.insert(self.cache[key]) # move to fron (most recently used)

            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        # remove it if it already exists because its going to the front now
        # as it is now most recently used
        if key in self.cache:
            self.remove(self.cache[key])
        # create the node and put it in
        self.cache[key] = Node(key, value) 
        self.insert(self.cache[key])

        # remove LRU if capacity surpassed
        if len(self.cache) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
