# You are given a sorted array consisting of only integers where every element 
# appears exactly twice, except for one element which appears exactly once. 
# 
#  Return the single element that appears only once. 
# 
#  Your solution must run in O(log n) time and O(1) space. 
# 
#  
#  Example 1: 
#  Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
#  
#  Example 2: 
#  Input: nums = [3,3,7,7,10,11,11]
# Output: 10
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  0 <= nums[i] <= 10⁵ 
#  
# 
#  Related Topics Array Binary Search 👍 11145 👎 190

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid % 2 != 0:  # mid is odd num
                if nums[mid - 1] == nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:  # mid is even num
                if nums[mid + 1] == nums[mid]:
                    left = mid + 2
                else:
                    right = mid
        return nums[left]


# leetcode submit region end(Prohibit modification and deletion)
# test from here
print(Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2)
print(Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10)
print(Solution().singleNonDuplicate([1]) == 1)
print(Solution().singleNonDuplicate([1, 1, 2]) == 2)
