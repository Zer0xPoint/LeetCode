from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_i = 0
        odd_i = len(A) - 1
        res_list = [0] * len(A)
        for i in A:
            if i % 2 == 0:
                res_list[even_i] = i
                even_i += 1
            else:
                res_list[odd_i] = i
                odd_i -= 1
        # i = 0
        # j = len(A) - 1
        # while i < len(A) - 1 and j < 0:
        #     if A[i] % 2 != 0:
        #


        return res_list


if __name__ == "__main__":
    s = Solution()
    # arr = [0, 1, 0, 3, 12]
    # arr = [3, 5, 5]
    # arr = [1]
    # arr = [1, 0]
    arr = [3, 1, 2, 4]
    print(s.sortArrayByParity(arr))
    # print(arr)
