class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = [c for c in s.lower() if c.isalnum()]
        # for i in range(len(clean_s)):
        #     if clean_s[i] is not clean_s[len(clean_s) - i - 1]:
        #         return False
        # return True
        return clean_s == clean_s[::-1]


if __name__ == '__main__':
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    # s = "0P"
    print(solution.isPalindrome(s))
