class Solution:

    def encode(self, strs: List[str]) -> str:
        return '€'.join([str(len(strs)), *strs])

    def decode(self, s: str) -> List[str]:
        l = s.split('€')
        k = int(l[0])
        return l[1:k+1]
