class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = []
        for token in tokens:
            try:
                values.append(int(token))
            except ValueError:
                assert token in "+-*/", token
                tgt = values.pop()
                src = values.pop()
                if token == '+':
                    values.append(src + tgt)
                elif token == '-':
                    values.append(src - tgt)
                elif token == '*':
                    values.append(src * tgt)
                else:
                    values.append(int(src / tgt))
        return values.pop()
