# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None: return None
        hare, turtle = head, head
        while hare is not None:
            turtle = turtle.next
            hare = hare.next
            if hare is None: return None
            hare = hare.next
            if hare == turtle:
                turtle = head
                while turtle != hare:
                    hare = hare.next
                    turtle = turtle.next
                return hare
        return None


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


if __name__ == '__main__':
    nums = [3, 2, 0, -4]
    head = list_to_linked_list(nums)
    traverse_linked_list(head)
