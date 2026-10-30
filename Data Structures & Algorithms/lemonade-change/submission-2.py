class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hand = [0,0] # fives, tens
        for b in bills:
            if b == 5:
                hand[0] += 1
            if b == 10:
                if hand[0] == 0:
                    return False
                hand[1] += 1
                hand[0] -= 1
            if b == 20:
                if hand[1] > 0 and hand[0] > 0:
                    hand[1] -= 1
                    hand[0] -= 1
                elif hand[1] == 0 and hand[0] > 2:
                    hand[0] -= 3
                else:
                    return False

        return True