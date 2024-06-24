from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_dic = dict()
        for num in nums:
            count_dic[num] += 1
            if count_dic[num] > 1:
                count_dic.pop(num)

        return count_dic.popitem()[0]


if __name__ == '__main__':
    List = [2, 2, 1, 3, 3]
    solution = Solution()
    print((solution.singleNumber(List)))
