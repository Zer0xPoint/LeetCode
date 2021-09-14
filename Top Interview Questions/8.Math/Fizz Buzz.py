from typing import List

'''
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
'''


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """

        Args:
            n:

        Returns:

        """

        # naive Solution
        # fizz_flag, buzz_flag = 1, 1
        # res_list = []
        # for i in range(1, n + 1):
        #     res = str(i)
        #     if fizz_flag == 3 and buzz_flag == 5:
        #         res = 'FizzBuzz'
        #         fizz_flag = 0
        #         buzz_flag = 0
        #     elif buzz_flag == 5:
        #         res = 'Buzz'
        #         buzz_flag = 0
        #     elif fizz_flag == 3:
        #         res = 'Fizz'
        #         fizz_flag = 0
        #
        #     fizz_flag += 1
        #     buzz_flag += 1
        #     res_list.append(res)
        # return res_list

        # append String Solution
        # divisible_by_3 = lambda x: x % 3 == 0
        # divisible_by_5 = lambda x: x % 5 == 0
        #
        # res_list = []
        #
        # for i in range(1, n + 1):
        #     res = ''
        #     if divisible_by_3(i):
        #         res += 'Fizz'
        #     if divisible_by_5(i):
        #         res += 'Buzz'
        #     if not res:
        #         res = str(i)
        #     res_list.append(res)
        # return res_list

        # hash Solution
        divisible_hash = {3: 'Fizz', 5: 'Buzz'}

        res_list = []
        for i in range(1, n + 1):
            res = ''
            for key in divisible_hash.keys():
                if i % key == 0:
                    res += divisible_hash[key]
            if not res:
                res = str(i)
            res_list.append(res)
        return res_list


s = Solution()
print(s.fizzBuzz(100))
