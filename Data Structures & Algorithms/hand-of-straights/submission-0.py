class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        c = Counter(hand)
        while c:
            m = min(c)
            for i in range(m, m + groupSize):
                if i not in c:
                    return False
                c[i] -= 1
                if c[i] == 0:
                    del c[i]

        return True
