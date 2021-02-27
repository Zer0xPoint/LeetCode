# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        while n > 0:
            n -= 1
            if n == 0:
                tmp_node =


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
    head = list_to_linked_list(nums)
    n = 2
    s = Solution()
    print(s.removeNthFromEnd(head, n))
