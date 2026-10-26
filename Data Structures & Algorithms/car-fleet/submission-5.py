class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [(target - p) / s for p, s in cars]

        stack = []
        for time in reversed(times):
            if not stack:
                stack.append(time)
            elif stack and stack[-1] < time:
                stack.append(time)
        return len(stack)
