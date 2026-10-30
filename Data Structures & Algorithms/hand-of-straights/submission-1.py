class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        c = Counter(hand)
        for card in hand:
            if c[card] == 0:
                continue
            for i in range(card, card + groupSize):
                if i not in c:
                    return False
                c[i] -= 1

        return True
