from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # for i in range(0, len(arr)):
        #     if (arr[i] * 2 in arr[i + 1:]) or (arr[i] / 2 in arr[i + 1:]):
        #         print(i)
        #         return True
        # return False
        # hash_table
        seen = set()
        for i in arr:
            if i * 2 in seen or i / 2 in seen:
                return True
            seen.add(i)
        return False


if __name__ == '__main__':
    solution = Solution()
    # arr = [10, 2, 5, 3]
    # arr = [-2, 0, 10, -19, 4, 6, -8]
    arr = [0, 0]

    print(solution.checkIfExist(arr))
