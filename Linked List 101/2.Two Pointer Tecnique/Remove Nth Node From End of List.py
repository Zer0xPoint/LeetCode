# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head_node: ListNode, n: int) -> ListNode:
        # O(2n) Two Pass Solution
        # linked_list_len = 0
        # dummy_node = ListNode
        # dummy_node.next = head_node
        # while head_node:
        #     linked_list_len += 1
        #     head_node = head_node.next
        # count = linked_list_len - n
        # head_node = dummy_node
        # while count:
        #     count -= 1
        #     head_node = head_node.next
        # head_node.next = head_node.next.next
        # return dummy_node.next

        # One Pass Solution
        dummy_node = ListNode
        dummy_node.next = head_node
        first_node = dummy_node
        second_node = dummy_node

        for _ in range(n):
            first_node = first_node.next
        while first_node.next:
            first_node = first_node.next
            second_node = second_node.next
        second_node.next = second_node.next.next
        return dummy_node.next


def list_to_linked_list(array_list):
    head_node = ListNode(array_list[0])
    node = head_node
    for i in range(1, len(array_list)):
        node.next = ListNode(array_list[i])
        node = node.next
    return head_node


def traverse_linked_list(linked_list_head: ListNode):
    while linked_list_head:
        print(linked_list_head.val)
        linked_list_head = linked_list_head.next


def create_circle_in_linked_list(linked_list_head: ListNode, index: int):
    # traverse to tail
    tail_node = linked_list_head
    while tail_node.next:
        tail_node = tail_node.next
    # create circle at index
    head_node = linked_list_head
    for i in range(index):
        head_node = head_node.next
    tail_node.next = head_node


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    # nums = [1]
    head = list_to_linked_list(nums)
    n = 2
    # n = 1
    s = Solution()
    print(traverse_linked_list(s.removeNthFromEnd(head, n)))
