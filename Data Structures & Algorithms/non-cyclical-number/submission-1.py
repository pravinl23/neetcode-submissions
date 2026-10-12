class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum([int(x) ** 2 for x in str(n)])

        return True
        '''
        def nxt(i):
            return sum([int(x) ** 2 for x in str(i)])

        slow, fast = n, nxt(n)

        while fast != 1 and slow != fast:
            slow = nxt(slow)
            fast = nxt(nxt(fast))

        return fast == 1