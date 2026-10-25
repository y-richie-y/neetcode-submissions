class Solution:
    def trap(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        left_max = heights[left]
        right_max = heights[right]

        total = 0
        while left < right:
            if left_max < right_max:
                total += left_max - heights[left]
                left += 1
                left_max = max(left_max, heights[left])
            else:
                total += right_max - heights[right]
                right -= 1
                right_max = max(right_max, heights[right])
        return total

            



