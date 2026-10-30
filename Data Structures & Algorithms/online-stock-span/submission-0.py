class StockSpanner:

    def __init__(self):
        self.stack = [] # price, prevdays

    def next(self, price: int) -> int:
        stack = self.stack
        count = 0
        while stack and stack[-1][0] <= price:
            count += stack.pop()[1]
        stack.append([price, count + 1])
        return count + 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)