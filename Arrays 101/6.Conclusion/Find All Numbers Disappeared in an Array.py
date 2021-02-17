from typing import List

from pip._vendor.msgpack.fallback import xrange


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # full_nums_set = set(i for i in range(1, len(nums) + 1))
        # for i in set(nums):
        #     if i in nums:
        #         full_nums_set.remove(i)
        #
        # return list(full_nums_set)

        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == '__main__':
    s = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(s.findDisappearedNumbers(nums))
