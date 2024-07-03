from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_i = max(arr)
        for i in range(0, len(arr)):
            if arr[i] == max_i and i < len(arr) - 1:
                max_i = max(arr[i + 1:])
            arr[i] = max_i
            if i == len(arr) - 1:
                arr[i] = -1

        return arr


if __name__ == "__main__":
    s = Solution()
    arr = [17, 18, 5, 4, 6, 1]
    # arr = [3, 5, 5]
    print(s.replaceElements(arr))
