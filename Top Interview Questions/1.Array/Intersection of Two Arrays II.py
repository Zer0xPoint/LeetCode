from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # sort solution
        # nums1.sort()
        # nums2.sort()
        # result = []
        # i1, i2 = 0, 0
        #
        # while i1 < len(nums1) and i2< len(nums2):
        #     if nums1[i1] == nums2[i2]:
        #         result.append(nums1[i1])
        #         i1 += 1
        #         i2 += 1
        #     elif nums1[i1] < nums2[i2]:
        #         i1 += 1
        #     else:
        #         i2 += 1
        #
        # return result

        # hashmap solution
        result = []
        nums1_dict = defaultdict(int)
        for num in nums1:
            nums1_dict[num] += 1

        for num in nums2:
            if num in nums1_dict and nums1_dict[num] > 0:
                result.append(num)
                nums1_dict[num] -= 1

        return result


if __name__ == '__main__':
    s = Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(s.intersect(nums1, nums2))
