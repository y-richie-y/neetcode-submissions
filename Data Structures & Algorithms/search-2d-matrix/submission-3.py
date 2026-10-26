class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        step = 1 << 20
        while step:
            if i + step < len(matrix) and matrix[i + step][0] <= target:
                i += step
            step //= 2
        
        j = 0
        step = 1 << 20
        while step:
            if j + step < len(matrix[i]) and matrix[i][j + step] <= target:
                j += step
            step //= 2

        return matrix[i][j] == target
        