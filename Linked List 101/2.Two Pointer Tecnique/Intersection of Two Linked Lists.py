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
    def getIntersectionNode(self, A, B):
        if not A or not B: return None

        # Concatenate A and B
        last = A
        while last.next: last = last.next
        last.next = B

        # Find the start of the loop
        fast = slow = A
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                fast = A
                while fast != slow:
                    slow, fast = slow.next, fast.next
                last.next = None
                return slow

        # No loop found
        last.next = None
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
    nums = [3, 2, 0, -4]
    head = list_to_linked_list(nums)
    create_circle_in_linked_list(head, 0)
    # traverse_linked_list(head)
    list_a = [4, 1, 8, 4, 5]
    list_b = [2, 5, 6, 1, 8, 4, 5]
    list_a = [1, 8, 4, 5]
    list_b = [2, 3, 8, 4, 5]
    s = Solution()
    head_a = list_to_linked_list(list_a)
    head_b = list_to_linked_list(list_b)
    print(s.getIntersectionNode(head_a, head_b))
