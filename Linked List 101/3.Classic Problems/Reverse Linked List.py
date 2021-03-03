from ListNode import *


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pass


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    # nums = [1]
    head = list_to_linked_list(nums)
    s = Solution()
    print(traverse_linked_list(s.reverseList(head)))
