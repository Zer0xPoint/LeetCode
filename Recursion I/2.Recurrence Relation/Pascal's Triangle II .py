from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        nums = [0 for i in range(rowIndex + 1)]
        nums[0] = 1
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                nums[j] = nums[j] + nums[j - 1]
        return nums

