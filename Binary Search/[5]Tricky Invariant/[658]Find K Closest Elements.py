# Given a sorted integer array arr, two integers k and x, return the k closest 
# integers to x in the array. The result should also be sorted in ascending order. 
# 
# 
#  An integer a is closer to x than an integer b if: 
# 
#  
#  |a - x| < |b - x|, or 
#  |a - x| == |b - x| and a < b 
#  
# 
#  
#  Example 1: 
#  Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
#  
#  Example 2: 
#  Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
#  
#  
#  Constraints: 
# 
#  
#  1 <= k <= arr.length 
#  1 <= arr.length <= 10⁴ 
#  arr is sorted in ascending order. 
#  -10⁴ <= arr[i], x <= 10⁴ 
#  
# 
#  Related Topics Array Two Pointers Binary Search Sliding Window Sorting Heap (
# Priority Queue) 👍 8135 👎 685

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the closest element to x by binary search
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        # find the k closest elements by two pointers
        # left is the index of the closest element to x
        left, right = left - 1, left
        # when the window is expanded to k elements, the loop stops
        while right - left - 1 < k:
            # edge cases
            # if left < 0, the window is expanded to the right
            if left < 0:
                right += 1
            # if right == len(arr), the window is expanded to the left
            elif right == len(arr):
                left -= 1
            # if the distance between the left element and x is smaller than the distance between the right element and x
            elif x - arr[left] <= arr[right] - x:
                left -= 1
            # if the distance between the left element and x is larger than the distance between the right element and x
            else:
                right += 1
        return arr[left + 1:right]
# leetcode submit region end(Prohibit modification and deletion)
# test from here
print(Solution().findClosestElements([1,2,3,4,5], 4, 3)) # [1,2,3,4]
print(Solution().findClosestElements([1,2,3,4,5], 4, -1)) # [1,2,3,4]
print(Solution().findClosestElements([1,2,3,4,5], 4, 6)) # [2,3,4,5]
