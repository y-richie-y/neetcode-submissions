class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = sorted([
            (x, i) for i, x in enumerate(nums)
        ])

        index_mapping = {
            idx: i for idx, (_, i) in enumerate(new_nums)
        }

        nums = [x for x, _ in new_nums]
        start = 0
        end = len(nums) - 1
        while start < end:
            total = nums[end] + nums[start]
            if total > target:
                end -= 1
            elif total < target:
                start += 1
            else:
                # equals
                ans = [index_mapping[start], index_mapping[end]]
                return sorted(ans)
        raise ValueError("Solution doesn't exist")