from collections import deque, Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        window = deque()

        best_len = 0
        for ss in s:
            counts[ss] += 1
            window.append(ss)
            highest_count = max(counts.values())
            while len(window) - highest_count > k:
                counts[window.popleft()] -= 1
                highest_count = max(counts.values())
            best_len = max(best_len, len(window))
        return best_len


            
        