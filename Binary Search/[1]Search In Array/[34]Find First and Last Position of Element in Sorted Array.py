# Given an array of integers nums sorted in non-decreasing order, find the 
# starting and ending position of a given target value. 
# 
#  If target is not found in the array, return [-1, -1]. 
# 
#  You must write an algorithm with O(log n) runtime complexity. 
# 
#  
#  Example 1: 
#  Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#  
#  Example 2: 
#  Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#  
#  Example 3: 
#  Input: nums = [], target = 0
# Output: [-1,-1]
#  
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  nums is a non-decreasing array. 
#  -10⁹ <= target <= 10⁹ 
#  
# 
#  Related Topics Array Binary Search 👍 20372 👎 513

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)
        return [left, right]

    def binary_search(self, lst, target, leftmost=True):
        left, right = 0, len(lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if lst[mid] == target:
                if leftmost:
                    right = mid - 1
                else:
                    left = mid + 1
            elif lst[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left if leftmost else right


# leetcode submit region end(Prohibit modification and deletion)
# test from here
print(Solution().searchRange([5, 7, 7, 8, 8, 8, 8, 8, 8, 10], 8))  # [3,8]
print(Solution().searchRange([5, 7, 7, 8, 8, 8, 8, 8, 8, 10, 10], 8))  # [3,8]
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))  # [-1,-1]
