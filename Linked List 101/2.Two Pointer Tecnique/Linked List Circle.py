# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def hasCycle(self, head: ListNode) -> bool:
    #     if head is not None:
    #         return False
    #     walker = head
    #     runner = head
    #     while runner.next is not None and runner.next.next is not None:
    #         walker = walker.next
    #         runner = runner.next.next
    #     if walker == runner:
    #         return True
    #     return False

    def hasCycle(self, head: ListNode) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
