# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None:
            return None
        hare_node, turtle_node = head, head
        while hare_node and hare_node.next:
            turtle_node = turtle_node.next
            # hare_node = hare_node.next
            # if hare_node is None:
            #     return None
            # hare_node = hare_node.next
            hare_node = hare_node.next.next
            if hare_node is turtle_node:
                turtle_node = head
                while turtle_node != hare_node:
                    hare_node = hare_node.next
                    turtle_node = turtle_node.next
                return hare_node
        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_a, node_b = headA, headB
        while node_a != node_b:
            node_a = node_a.next if node_a is not None else node_b
            node_b = node_b.next if node_b is not None else node_a

        return node_a


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
    list_b = [1, 8, 4, 5]
    s = Solution()
    # print(s.detectCycle(head))
    head_a = list_to_linked_list(list_a)
    head_b = list_to_linked_list(list_b)
    print(s.getIntersectionNode(head_a, head_b))
