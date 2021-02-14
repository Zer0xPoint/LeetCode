class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start, end, num_count = 0, 0, 0
        while end < len(nums):
            if nums[end] > nums[start]:
                num_count += 1
                nums[num_count] = nums[end]
                start = end
            end += 1
        return num_count + 1