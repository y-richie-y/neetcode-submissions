class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(ss for ss in s if ss.isalnum())
        return s == s[::-1]
