from collections import Counter


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0: len(prefix) - 1]
                if not prefix:
                    return ""
        return prefix


if __name__ == '__main__':
    l = ["flower", "flow", "flight"]
    # l = ["dog", "racecar", "car"]
    # l = ["", ""]
    s = Solution()
    print(s.longestCommonPrefix(l))
