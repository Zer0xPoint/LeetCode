class Solution(object):
    def kthGrammar(self, N, K):
        if N == 1:
            if K == 1:
                return 0
            else:
                return 1

        half = 2 ** (N - 1)
        if K <= half:
            return self.kthGrammar(N - 1, K)
        else:
            res = self.kthGrammar(N - 1, K - half)
            if res == 0:
                return 1
            else:
                return 0
