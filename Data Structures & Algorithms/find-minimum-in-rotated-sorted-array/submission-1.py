class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        step = 1 << len(nums).bit_length()
        while step:
            if i + step < len(nums) and nums[0] < nums[i + step]:
                i += step
            step //= 2
        
        return nums[(i + 1) % len(nums)]