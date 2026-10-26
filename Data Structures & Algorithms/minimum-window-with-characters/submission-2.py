from collections import Counter, deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        if not Counter(s) >= Counter(t):
            return ""
        counter = Counter()
        window = deque()
        formed = 0
        required = len(set(t))

        best = (0, len(s))
        for i, ss in enumerate(s):
            window.append(ss)
            counter[ss] += 1
            if counter[ss] == counter_t[ss]:
                formed += 1

            while formed == required:
                if len(window) < (best[1] - best[0]):
                    best = (i+1 - len(window), i+1)
                left_char = window.popleft()
                counter[left_char] -= 1
                if counter[left_char] + 1 == counter_t[left_char]:
                    formed -= 1
        return s[best[0]:best[1]]
