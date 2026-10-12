class TimeMap:

    def __init__(self):
        self.timemap = {} # {key : [[time][value]]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = [[],[]]
        self.timemap[key][0].append(timestamp)
        self.timemap[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""

        times = self.timemap[key][0]
        values = self.timemap[key][1]
        r = len(times) - 1
        while r >= 0:
            if times[r] > timestamp:
                r -= 1
            else:
                return values[r]
        return ""

