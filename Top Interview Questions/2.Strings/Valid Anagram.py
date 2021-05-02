from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for i in range(len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1

        return s_dict == t_dict


if __name__ == '__main__':
    solution = Solution()
    s = "loveleetcode"
    t = "loveleetcade"
    print(solution.isAnagram(s, t))
