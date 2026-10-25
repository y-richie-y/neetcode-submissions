from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            canon_s = ''.join(sorted(s))
            anagrams[canon_s].append(s)
        return list(anagrams.values())
            
            
