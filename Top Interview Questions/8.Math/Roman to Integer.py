class Solution:
    def romanToInt(self, s: str) -> int:
        roman_symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        prev= 0
        for i in s[::-1]:
            curr = roman_symbol[i]
            if prev > curr:
                res -= curr
            else:
                res += curr
            prev = curr
        return res
