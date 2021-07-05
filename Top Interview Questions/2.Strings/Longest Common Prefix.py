from collections import Counter


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or len(strs) < 1:
            return [""]
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(len(strs)):
                if i is len(strs[j]) or strs[j][i] != c:
                    return strs[0][:i]


if __name__ == '__main__':
    l = ["flower", "flow", "flight"]
    # l = ["dog", "racecar", "car"]
    l = ["a"]
    s = Solution()
    print(s.longestCommonPrefix(l))
