from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        nums_dict = defaultdict(int)
        for index, num in enumerate(nums):
            nums_dict[num] = index

        for index in range(len(nums_dict)):
            minus = target - nums[index]
            if minus in nums_dict.keys() and nums_dict[minus] != index:
                return [index, nums_dict[minus]]        

if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    nums = [3, 2, 4]
    #nums = [3, 3]
    target = 9
    target = 6
    print(s.twoSum(nums, target))
