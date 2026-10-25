class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        for i, num in enumerate(nums):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                total = num + nums[start] + nums[end]
                if total > 0:
                    end -= 1
                elif total < 0:
                    start += 1
                else:
                    ans.add((num, nums[start], nums[end]))
                    start += 1
        ans = [list(t) for t in ans]
        return ans
