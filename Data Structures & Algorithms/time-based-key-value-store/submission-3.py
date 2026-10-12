class TimeMap:

    def __init__(self):
        self.tm = {} # key : [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tm:
            self.tm[key] = []
        self.tm[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm:
            return ""
        storage = self.tm[key]
        l, r = 0, len(storage) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if storage[m][1] == timestamp:
                return storage[m][0]
            if storage[m][1] > timestamp:
                r = m - 1
            elif storage[m][1] < timestamp:
                res = storage[m][0]
                l = m + 1
        return res
            
