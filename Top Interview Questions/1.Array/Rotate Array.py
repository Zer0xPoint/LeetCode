from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse_list(origin_list, start, end):
            while start < end:
                origin_list[start], origin_list[end] = origin_list[end], origin_list[start]
                start += 1
                end -= 1

        n = len(nums)
        k %= n

        if n == 0:
            return
        else:
            nums.reverse()
            reverse_list(nums, 0, k - 1)
            reverse_list(nums, k, n - 1)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    k = 2
    s.rotate(nums, k)
    print(nums)