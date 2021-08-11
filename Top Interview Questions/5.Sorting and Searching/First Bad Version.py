# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    if version > 3:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        def binary_search(start, end):
            if end >= 1:
                # mid = start + (end - 1) // 2
                mid = (start + end) // 2
                if isBadVersion(mid):
                    if not isBadVersion(mid - 1):
                        return mid
                    else:
                        return binary_search(start, mid - 1)
                else:
                    return binary_search(mid + 1, end)
            else:
                return -1

        return binary_search(1, n)


if __name__ == '__main__':
    n = 4

    s = Solution()
    print(s.firstBadVersion(n))
