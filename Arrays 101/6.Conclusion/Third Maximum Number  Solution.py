from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_set = set()
        max_set.add(nums[0])
        for num in nums:
            max_set.add(num)
            if len(max_set) > 3:
                max_set.remove(min(max_set))

        max_list = list(max_set)

        return min(max_list) if len(max_list) > 2 else max(max_list)


if __name__ == '__main__':
    s = Solution()
    arr = [1, 1, 4, 2, 1, 3]
    # arr = [1, 2]
    # arr = [1, 1, 2]
    # arr = [2, 2, 3, 1]
    print(s.thirdMax(arr))
