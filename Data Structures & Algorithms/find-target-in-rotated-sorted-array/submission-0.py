class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find offset first

        i = 0
        step = 1 << len(nums).bit_length()
        while step:
            if i + step < len(nums) and nums[0] < nums[i + step]:
                i += step
            step //= 2
        offset = (i + 1) % len(nums)

        def value(i):
            # if not 0 <= i < len(nums):
            #     raise ValueError("Index out of range")
            return nums[(i + offset) % len(nums)]
        
        i = 0
        step = 1 << len(nums).bit_length()
        while step:
            if i + step < len(nums) and value(i + step) <= target:
                i += step
            step //= 2
        
        if value(i) == target:
            return (i + offset) % len(nums)
        return -1

        

