from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()

        ans = []
        for idx, num in enumerate(nums):
            while window and window[-1][1] < num:
                window.pop()
            window.append((idx, num))
            while window[0][0] <= idx - k:
                window.popleft()
            
            if idx >= k - 1:
                ans.append(window[0][1])
        return ans



            
