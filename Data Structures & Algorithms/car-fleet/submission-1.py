class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)

        fleets = 0
        lead = 0
        for pos, spd in cars:
            arrival = (target-pos) / spd
            if arrival > lead:
                fleets += 1
                lead = arrival

        return fleets
            





        