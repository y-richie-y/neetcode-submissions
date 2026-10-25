class Solution:
    def trap(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        left_max = heights[left]
        right_max = heights[right]

        total = 0
        while left < right:
            if heights[left] < heights[right]:
                total += max(0, min(left_max, right_max) - heights[left])
                left += 1
                left_max = max(left_max, heights[left])
            else:
                total += max(0, min(left_max, right_max) - heights[right])
                right -= 1
                right_max = max(right_max, heights[right])
        return total

            



