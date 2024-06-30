# Given an array arr of positive integers sorted in a strictly increasing order,
#  and an integer k. 
# 
#  Return the kᵗʰ positive integer that is missing from this array. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5
# ᵗʰ missing positive integer is 9.
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2ⁿᵈ missing 
# positive integer is 6.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 1000 
#  1 <= arr[i] <= 1000 
#  1 <= k <= 1000 
#  arr[i] < arr[j] for 1 <= i < j <= arr.length 
#  
# 
#  
#  Follow up: 
# 
#  Could you solve this problem in less than O(n) complexity? 
# 
#  Related Topics Array Binary Search 👍 6575 👎 443

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # # build a list that length equals to the length of arr + k
        # full_num = [i for i in range(1, len(arr) + k + 1)]
        # for i in arr:
        #     if i in full_num:
        #         full_num.remove(i)
        # return full_num[k - 1]

        # binary search
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            # the number of missing numbers before arr[mid] is less than k
            if (missing := arr[mid] - mid - 1) < k:
                left = mid + 1
            else:
                right = mid
        return right + k


# leetcode submit region end(Prohibit modification and deletion)
# test from here
print(Solution().findKthPositive([2, 3, 4, 7, 11], 5))
print(Solution().findKthPositive([1, 2, 3, 4], 2))
print(Solution().findKthPositive([1], 2))
# long test
print(Solution().findKthPositive([i for i in range(1, 1001)], 1000))
