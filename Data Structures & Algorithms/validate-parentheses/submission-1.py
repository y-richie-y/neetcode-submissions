class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', ']': '[', '}': '{'}

        stack = []
        for ss in s:
            if ss in '([{':
                stack.append(ss)
            else:
                assert ss in ')]}'
                if not stack or stack[-1] != bracket_map[ss]:
                    return False
                stack.pop()
        
        return not stack
