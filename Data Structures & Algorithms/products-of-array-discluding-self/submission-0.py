from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = []
        factor = 1
        for num in nums:
            left_prod.append(factor)
            factor *= num
        
        right_prod = []
        factor = 1
        for num in nums[::-1]:
            right_prod.append(factor)
            factor *= num
        ans = []
        for left, right in zip(left_prod, right_prod[::-1]):
            ans.append(left * right)
        return ans
