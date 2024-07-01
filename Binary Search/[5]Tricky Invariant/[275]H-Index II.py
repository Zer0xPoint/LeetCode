# Given an array of integers citations where citations[i] is the number of 
# citations a researcher received for their iᵗʰ paper and citations is sorted in 
# ascending order, return the researcher's h-index. 
# 
#  According to the definition of h-index on Wikipedia: The h-index is defined 
# as the maximum value of h such that the given researcher has published at least 
# h papers that have each been cited at least h times. 
# 
#  You must write an algorithm that runs in logarithmic time. 
# 
#  
#  Example 1: 
# 
#  
# Input: citations = [0,1,3,5,6]
# Output: 3
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each 
# of them had received 0, 1, 3, 5, 6 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the 
# remaining two with no more than 3 citations each, their h-index is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: citations = [1,2,100]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  n == citations.length 
#  1 <= n <= 10⁵ 
#  0 <= citations[i] <= 1000 
#  citations is sorted in ascending order. 
#  
# 
#  Related Topics Array Binary Search 👍 335 👎 91

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # for i in range(len(citations) - 1, -1, -1):  # index from the end of the list to the beginning
        #     if citations[i] < len(citations) - i: # if the number of citations is less than the number of papers
        #         return len(citations) - i - 1
        # return len(citations)

        # binary search
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            # if the number of citations is greater than or equal to the number of papers
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1
        return n - left


# leetcode submit region end(Prohibit modification and deletion)
# test from here
print(Solution().hIndex([0, 1, 3, 5, 6]) == 3)
# print(Solution().hIndex([1, 2, 100]) == 2)
# print(Solution().hIndex([100]))  # 1
print(Solution().hIndex([11, 15]))  # 2
