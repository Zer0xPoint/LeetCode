# You are given an array of intervals, where intervals[i] = [starti, endi] and 
# each starti is unique. 
# 
#  The right interval for an interval i is an interval j such that startj >= 
# endi and startj is minimized. Note that i may equal j. 
# 
#  Return an array of right interval indices for each interval i. If no right 
# interval exists for interval i, then put -1 at index i. 
# 
#  
#  Example 1: 
# 
#  
# Input: intervals = [[1,2]]
# Output: [-1]
# Explanation: There is only one interval in the collection, so it outputs -1.
#  
# 
#  Example 2: 
# 
#  
# Input: intervals = [[3,4],[2,3],[1,2]]
# Output: [-1,0,1]
# Explanation: There is no right interval for [3,4].
# The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start 
# that is >= end1 = 3.
# The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start 
# that is >= end2 = 2.
#  
# 
#  Example 3: 
# 
#  
# Input: intervals = [[1,4],[2,3],[3,4]]
# Output: [-1,2,-1]
# Explanation: There is no right interval for [1,4] and [3,4].
# The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start 
# that is >= end1 = 3.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= intervals.length <= 2 * 10⁴ 
#  intervals[i].length == 2 
#  -10⁶ <= starti <= endi <= 10⁶ 
#  The start point of each interval is unique. 
#  
# 
#  Related Topics Array Binary Search Sorting 👍 2135 👎 352

from bisect import bisect_left
from math import inf
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # sorted_intervals = sorted(intervals)
        sorted_intervals = sorted((start, i) for i, (start, _) in enumerate(intervals))
        result = [-1] * (len(intervals))
        for i, (_, end) in enumerate(intervals):
            # use bisect_left to find the first element >= end
            j = bisect_left(sorted_intervals, (end, -inf))
            if j < len(intervals):
                result[i] = sorted_intervals[j][1]
        return result

        # leetcode submit region end(Prohibit modification and deletion)


# test from here
print(Solution().findRightInterval([[1, 4], [2, 3], [3, 4]]))  # [-1,2,-1]
