class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result_list = []
        # for i in range(len(nums), 0):
        i = 0
        j = len(nums) - 1
        while i <= j:
            pre_squ = nums[i] ** 2
            last_squ = nums[j] ** 2
            if pre_squ < last_squ:
                result_list.insert(0, last_squ)
                j -= 1
            else:
                result_list.insert(0, pre_squ)
                i += 1
        return result_list