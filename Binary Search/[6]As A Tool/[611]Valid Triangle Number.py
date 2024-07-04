# Given an integer array nums, return the number of triplets chosen from the 
# array that can make triangles if we take them as side lengths of a triangle. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [4,2,3,4]
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 1000 
#  0 <= nums[i] <= 1000 
#  
# 
#  Related Topics Array Two Pointers Binary Search Greedy Sorting 👍 3803 👎 215
# 

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # sort the list
        nums.sort()
        count = 0
        # i is the longest side, change it from the end to the beginning, for example, 4,3,2,1
        for i in range(len(nums) - 1, 1, -1):
            left, right = 0, i - 1
            while left < right:
                # if the sum of the two sides is greater than the longest side, it is a triangle
                if nums[left] + nums[right] > nums[i]:
                    # any side between left and right can be used as the second side, so the number of triangles is right - left
                    # for example, 2,2,3,4, when i=3, left=0, right=2, the number of triangles is 2-0=2
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count


# leetcode submit region end(Prohibit modification and deletion)
# test from here
print(Solution().triangleNumber(
    [2, 2, 3, 4]))  # 3 explanation: 2,3,4 (using the first 2), 2,3,4 (using the second 2), 2,2,3
print(Solution().triangleNumber([4, 2, 3, 4]))  # 4 explanation: 4,2,3, 4,2,4, 2,3,4, 2,3,4
