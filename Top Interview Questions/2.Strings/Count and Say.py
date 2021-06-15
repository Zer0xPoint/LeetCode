from collections import Counter


# 1.     1
#  2.     11
#  3.     21
#  4.     1211
#  5.     111221
#  6.     312211
#  7.     13112221
#  8.     1113213211
#  9.     31131211131221
# 10.     13211311123113112211


class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        # if n < 2:
        #     return res
        for _ in range(n - 1):
            curr = res[0]
            temp_res = ""
            count = 0
            for l in res:
                if curr is l:
                    # temp_res = l
                    count += 1
                else:
                    temp_res += str(count) + curr
                    curr = l
                    count = 1
            temp_res += str(count) + curr
            res = temp_res
        return res


if __name__ == '__main__':
    solution = Solution()
    n = 4
    print(solution.countAndSay(n))
