class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_len = len(nums)
        list_res = []
        i = 0
        j = list_len - 1

        while i == j:
            if nums[i] + nums[j] == target:
                list_res = [i, j]
            elif nums[i] + nums[j] < target:
                i = i + 1
            else:
                j = j - 1
        return list_res


# def stringToIntegerList(input):
#     return json.loads(input)
#
#
# def integerListToString(nums, len_of_list=None):
#     if not len_of_list:
#         len_of_list = len(nums)
#     return json.dumps(nums[:len_of_list])


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            # nums = stringToIntegerList(line);
            line = next(lines)
            target = int(line);

            ret = Solution().twoSum([2, 7, 11, 15], 9)

            # out = integerListToString(ret);
            print(ret)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
