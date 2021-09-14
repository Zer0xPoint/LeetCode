class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        汉明重量
        Args:
            n:

        Returns:

        '''
        return bin(n).count('1')


n = 11111111111111111111111111111101
s = Solution()
print(s.hammingWeight(n))
