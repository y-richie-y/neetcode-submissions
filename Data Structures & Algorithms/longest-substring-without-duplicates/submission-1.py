from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        window = deque()
        best = 0
        for ss in s:
            while ss in seen:
                seen.remove(window.popleft())
            seen.add(ss)
            window.append(ss)
            best = max(best, len(seen))
        return best
