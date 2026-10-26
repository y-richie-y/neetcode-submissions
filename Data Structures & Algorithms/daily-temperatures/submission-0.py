class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                idx, _ = stack.pop()
                ans[idx] = i - idx
            stack.append((i, temperature))
        return ans