from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False

        start_num = arr[0]
        end_num = arr[-1]

        for start in range(0, len(arr)):
            if start != 0 and arr[start] <= start_num:
                break
            else:
                start_num = arr[start]

        for end in range(len(arr) - 1, -1, -1):
            if end != len(arr) - 1 and arr[end] <= end_num:
                break
            else:
                end_num = arr[end]

        return start - 1 == end + 1 and start_num == end_num


if __name__ == "__main__":
    s = Solution()
    # arr = [1, 2, 2, 1]
    # arr = [1, 2, 1]
    # arr = [2, 0, 2]
    # arr = [1, 2]
    # arr = [0, 3, 2, 1]
    arr = [3, 5, 5]
    print(s.validMountainArray(arr))
