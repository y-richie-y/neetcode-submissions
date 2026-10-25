from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = sorted(Counter(nums).items(), key=lambda v: v[1])
        return [x for x, _ in counts[-k:]]
