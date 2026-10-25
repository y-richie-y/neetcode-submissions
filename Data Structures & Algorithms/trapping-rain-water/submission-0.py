class Solution:
    def trap(self, heights: List[int]) -> int:
        left_maxes = []
        left_max = 0
        for height in heights:
            left_max = max(height, left_max)
            left_maxes.append(left_max)
        
        right_maxes = []
        right_max = 0
        for height in heights[::-1]:
            right_max = max(height, right_max)
            right_maxes.append(right_max)
        right_maxes = right_maxes[::-1]

        total = 0
        for i, height in enumerate(heights):
            min_height = min(left_maxes[i], right_maxes[i])
            total += min_height - heights[i]
        return total
            



