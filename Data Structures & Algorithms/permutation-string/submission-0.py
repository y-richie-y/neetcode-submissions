from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counter1 = Counter(s1)
        counter = Counter(s2[:len(s1)])
        if counter1 == counter:
            return True
        for i in range(len(s1), len(s2)):
            counter[s2[i - len(s1)]] -= 1
            counter[s2[i]] += 1
            if counter1 == counter:
                return True
        return False

            
