import math

'''
3^x = n when x % 1 == 0
求是否n为3的整数次方

3^x = n
x = log3(n)
x = log(n)/log(3)
when x % 1 == 0 return True
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return (math.log10(n) / math.log10(3)) % 1 == 0 if n > 0 else False


s = Solution()
print(s.isPowerOfThree(243))
