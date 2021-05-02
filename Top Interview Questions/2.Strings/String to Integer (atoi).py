import re


class Solution(object):
    def myAtoi(self, s: str):
        s = s.strip()
        s = re.findall('(^[\+\-0]*\d+)\D*', s)
        try:
            result = int(''.join(s))
            max_int = 2147483647
            min_int = -2147483648
            if result > max_int > 0:
                return max_int
            elif result < min_int < 0:
                return min_int
            else:
                return result
        except:
            return 0
