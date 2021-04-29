from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last_nine_idx = len(digits)
        # for i in range(len(digits) - 1, -1, -1):
        #     if digits[i] == 9:
        #         last_nine -= 1
        #         digits[i] = 0
        #     else:
        #         break
        while last_nine_idx > 0 and digits[last_nine_idx - 1] == 9:
            digits[last_nine_idx - 1] = 0
            last_nine_idx -= 1

        if last_nine_idx == 0:
            digits.insert(0, 1)
        else:
            digits[last_nine_idx - 1] += 1
        return digits


if __name__ == '__main__':
    s = Solution()
    digits = [4, 3, 2, 1, 9, 9, 9]
    # digits = [9, 9, 9]
    digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    # digits = [9]
    print(s.plusOne(digits))
