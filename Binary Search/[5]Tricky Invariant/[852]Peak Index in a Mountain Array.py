# You are given an integer mountain array arr of length n where the values 
# increase to a peak element and then decrease. 
# 
#  Return the index of the peak element. 
# 
#  Your task is to solve it in O(log(n)) time complexity. 
# 
#  
#  Example 1: 
# 
#  
#  Input: arr = [0,1,0] 
#  
# 
#  Output: 1 
# 
#  Example 2: 
# 
#  
#  Input: arr = [0,2,1,0] 
#  
# 
#  Output: 1 
# 
#  Example 3: 
# 
#  
#  Input: arr = [0,10,5,2] 
#  
# 
#  Output: 1 
# 
#  
#  Constraints: 
# 
#  
#  3 <= arr.length <= 10⁵ 
#  0 <= arr[i] <= 10⁶ 
#  arr is guaranteed to be a mountain array. 
#  
# 
#  Related Topics Array Binary Search 👍 7470 👎 1916

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] > arr[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1
        return left


# leetcode submit region end(Prohibit modification and deletion)
# test from here
print(Solution().peakIndexInMountainArray([0, 1, 0]))  # 1
print(Solution().peakIndexInMountainArray([0, 2, 1, 0]))  # 1
print(Solution().peakIndexInMountainArray([0, 10, 5, 2]))  # 1
print(Solution().peakIndexInMountainArray([3, 4, 5, 1]))  # 2
