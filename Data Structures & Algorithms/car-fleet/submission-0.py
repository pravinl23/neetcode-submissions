class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        cars = cars[::-1]
        stack = []

        fleets = 0
        for pos, spd in cars:
            arrival = (target-pos) / spd
            if not stack:
                stack.append(arrival)
                continue
            if stack[-1] < arrival:
                stack.pop()
                fleets += 1
                stack.append(arrival)

        if stack:
            fleets += 1
        return fleets
            





        