from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        full_nums_set = set(i for i in range(1, len(nums) + 1))
        for i in set(nums):
            if i in nums:
                full_nums_set.remove(i)
        return list(full_nums_set)


if __name__ == '__main__':
    s = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(s.findDisappearedNumbers(nums))
