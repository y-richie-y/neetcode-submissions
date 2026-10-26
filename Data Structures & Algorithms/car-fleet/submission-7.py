class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))

        fleets = 0
        last_time = 0
        for p, s in reversed(cars):
            time = (target - p) / s
            if last_time < time:
                last_time = time
                fleets += 1
        return fleets
