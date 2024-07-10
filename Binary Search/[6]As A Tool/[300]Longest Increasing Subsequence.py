# Given an integer array nums, return the length of the longest strictly 
# increasing subsequence. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the 
# length is 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2500 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
#  Follow up: Can you come up with an algorithm that runs in O(n log(n)) time 
# complexity? 
# 
#  Related Topics Array Binary Search Dynamic Programming 👍 20804 👎 439
import bisect
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # 在寻找以nums[i] 结尾的最长递增子序列。
        # 如果 nums[j] < nums[i]，那么
        # nums[i] 可以接在 nums[j]后面形成一个更长的递增子序列。
        # 因此，我们需要更新
        # f[i]  为  f[j] + 1  和  f[i]  中的较大值，以确保 f[i]  始终是以  nums[i]  结尾的最长递增子序列的长度。
        # 举个例子：  假设
        # nums = [10, 9, 2, 5, 3, 7, 101, 18]，我们来看看
        # f
        # 数组的更新过程：
        # 初始时，f = [1, 1, 1, 1, 1, 1, 1, 1]，因为每个元素自身可以看作一个长度为
        # 1
        # 的递增子序列。
        # 当
        # i = 3
        # 时，nums[3] = 5：
        # j = 0，nums[0] = 10，nums[0] > nums[3]，不更新。
        # j = 1，nums[1] = 9，nums[1] > nums[3]，不更新。
        # j = 2，nums[2] = 2，nums[2] < nums[3]，更新
        # f[3] = max(f[3], f[2] + 1) = max(1, 1 + 1) = 2。
        # 此时，f = [1, 1, 1, 2, 1, 1, 1, 1]。
        # 当
        # i = 4
        # 时，nums[4] = 3：
        # j = 0，nums[0] = 10，nums[0] > nums[4]，不更新。
        # j = 1，nums[1] = 9，nums[1] > nums[4]，不更新。
        # j = 2，nums[2] = 2，nums[2] < nums[4]，更新
        # f[4] = max(f[4], f[2] + 1) = max(1, 1 + 1) = 2。
        # j = 3，nums[3] = 5，nums[3] > nums[4]，不更新。
        # 此时，f = [1, 1, 1, 2, 2, 1, 1, 1]。
        # 当
        # i = 5
        # 时，nums[5] = 7：
        # j = 0，nums[0] = 10，nums[0] > nums[5]，不更新。
        # j = 1，nums[1] = 9，nums[1] > nums[5]，不更新。
        # j = 2，nums[2] = 2，nums[2] < nums[5]，更新
        # f[5] = max(f[5], f[2] + 1) = max(1, 1 + 1) = 2。
        # j = 3，nums[3] = 5，nums[3] < nums[5]，更新
        # f[5] = max(f[5], f[3] + 1) = max(2, 2 + 1) = 3。
        # j = 4，nums[4] = 3，nums[4] < nums[5]，更新
        # f[5] = max(f[5], f[4] + 1) = max(3, 2 + 1) = 3。
        # 此时，f = [1, 1, 1, 2, 2, 3, 1, 1]。
        # 通过这种方式，可以逐步找到以每个元素结尾的最长递增子序列的长度。

        # n = len(nums)
        # dp = [1] * n
        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             # 如果 nums[i] 可以接在 nums[j] 后面形成一个更长的递增子序列，则更新 dp[i]
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp)

        # approach 2 binary search
        # 创建一个空数组，
        # 如果下一个数小于当前（二分左查找）的数，替换当前的数，
        # 如果大于最大的数，添加到数组末尾，
        # 这样能保证数组是递增的，且长度是最长的。
        sub_list = []
        for num in nums:
            # 找到 num 在 sub_list 中最先出现，大于等于 num 的数字的位置pos
            pos = bisect.bisect_left(sub_list, num)
            # 如果 pos == len(sub_list)，则 num 比 sub_list 中的所有元素都大，将 num 添加到 sub_list 末尾
            if pos == len(sub_list):
                sub_list.append(num)
            else:
                # 否则，用 num 覆盖掉 sub_list[pos]
                sub_list[pos] = num
        return len(sub_list)


# leetcode submit region end(Prohibit modification and deletion)
# test from here
print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4)
print(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4)
print(Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1)
