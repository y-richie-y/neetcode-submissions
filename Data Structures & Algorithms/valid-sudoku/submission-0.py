class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid9(values):
            if len(values) != 9:
                raise ValueError("Wrong number of items")
            if any(v not in '.123456789' for v in values):
                return False
            if any(v != '.' and c > 1 for v, c in Counter(values).items()):
                return False
            return True

        if any(not isValid9(row) for row in board):
            return False
        
        cols = [[board[j][i] for j in range(9)] for i in range(9)]
        if any(not isValid9(col) for col in cols):
            return False
        
        boxes = [
            [*board[i][j:j+3], *board[i+1][j:j+3], *board[i+2][j:j+3]]
            for i in [0, 3, 6] for j in [0, 3, 6]
        ]
        if any(not isValid9(box) for box in boxes):
            return False
        return True

        