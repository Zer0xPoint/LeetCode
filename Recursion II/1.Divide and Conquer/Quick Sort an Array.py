class Solution(object):
    def quick_sort(self, nums, start, end):

        def partition(start, end):
            pivot = nums[end]
            pivot_index = start
            for i in range(start, end):
                if nums[i] < pivot:
                    nums[pivot_index], nums[i] = nums[i], nums[pivot_index]
                    pivot_index += 1
            nums[end], nums[pivot_index] = nums[pivot_index], nums[end]
            return pivot_index

        if start < end:
            pivot_index = partition(start, end)
            self.quick_sort(nums, start, pivot_index - 1)
            self.quick_sort(nums, pivot_index + 1, end)
        # return pivot_index


s = Solution()
nums = [4, 3, 2, 5,1]
s.quick_sort(nums, start=0, end=len(nums) - 1)
print(nums)
