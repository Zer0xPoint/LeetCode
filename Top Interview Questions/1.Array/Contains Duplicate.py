from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len_list = len(nums)
        len_set = len(set(nums))
        return len_list != len_set


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    nums = [1, 2, 3, 4]
    print(s.containsDuplicate(nums))
