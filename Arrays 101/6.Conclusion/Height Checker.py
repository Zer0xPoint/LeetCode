from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        diff_count = 0
        for i in range(0, len(heights)):
            if heights[i] != sorted_heights[i]:
                diff_count += 1
        return diff_count


if __name__ == '__main__':
    s = Solution()
    arr = [1, 1, 4, 2, 1, 3]
    print(s.heightChecker(arr))
