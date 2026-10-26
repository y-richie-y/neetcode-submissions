class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        step = 1 << 20
        while step:
            if i + step < len(nums) and nums[i + step] <= target:
                i += step
            step //= 2
        
        if nums[i] == target:
            return i
        return -1
