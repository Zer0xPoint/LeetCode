from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        # hash table Solution
        # nums_dict = defaultdict(int)
        #
        # for num in nums:
        #     nums_dict[num] += 1
        # for i in nums_dict:
        #     if nums_dict[i] == 1:
        #         return i

        # bit manipulation
        # XOR
        # a xor 0 = a
        # a xor a = 0

        a = 0
        for num in nums:
            a ^= num
        return a


if __name__ == '__main__':
    s = Solution()
    nums = [4, 1, 2, 1, 2]
    print(s.singleNumber(nums))
