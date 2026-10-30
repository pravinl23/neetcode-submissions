class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        active = [0, 0] # D, R
        delete = [0, 0] # D, R
        for ch in senate:
            if ch == "D":
                active[0] += 1
            else:
                active[1] += 1
        i = 0
        senate = [ch for ch in senate]
        while active[0] != 0 and active[1] != 0:
            i = i % n
            if senate[i] == "D":
                if delete[0] > 0:
                    delete[0] -= 1
                    active[0] -= 1
                    senate[i] = "S"
                else:
                    delete[1] += 1
            elif senate[i] == "R":
                if delete[1] > 0:
                    delete[1] -= 1
                    active[1] -= 1
                    senate[i] = "S"
                else:
                    delete[0] += 1
            i += 1
        if active[0] == 0:
            return "Radiant"
        else:
            return "Dire"
