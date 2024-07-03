from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # even_i = 0
        # odd_i = len(A) - 1
        # res_list = [0] * len(A)
        # for i in A:
        #     if i % 2 == 0:
        #         res_list[even_i] = i
        #         even_i += 1
        #     else:
        #         res_list[odd_i] = i
        #         odd_i -= 1
        # return res_list

        # In-Place Solution
        even_i = 0
        odd_i = len(A) - 1
        while even_i < odd_i:
            if A[even_i] % 2 == 0 and A[odd_i] % 2 == 0:
                odd_i -= 1
            elif A[even_i] % 2 != 0 and A[odd_i] % 2 != 0:
                even_i += 1
            elif A[even_i] % 2 != 0 and A[odd_i] % 2 == 0:
                tmp = A[odd_i]
                A[odd_i] = A[even_i]
                A[even_i] = tmp
                even_i += 1
                odd_i -= 1
            else:
                even_i += 1
                odd_i -= 1
        return A


if __name__ == "__main__":
    s = Solution()
    # arr = [0, 1, 0, 3, 12]
    # arr = [3, 5, 5]
    # arr = [1]
    # arr = [1, 0]
    arr = [5, 6, 7, 3, 1, 2, 4, 8, 9]
    print(s.sortArrayByParity(arr))
    # print(arr)
