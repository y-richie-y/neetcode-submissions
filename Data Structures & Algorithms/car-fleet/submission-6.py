class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [(target - p) / s for p, s in cars]

        fleets = 0
        last_time = 0
        for time in reversed(times):
            if last_time < time:
                last_time = time
                fleets += 1
        return fleets
