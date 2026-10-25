class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best_length = 0
        for num in nums:
            if num-1 in nums_set:
                continue
            c = num + 1
            while c in nums_set:
                c += 1
            length = c - num
            best_length = max(length, best_length)
        return best_length

