# # Definition for a Node.
# class Node:
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child
#
#
# class Solution:
#     def flatten(self, head: 'Node') -> 'Node':
#         pass
#
#
# def create_doubly_linked_list(nums, head_node):
#     # dummy_head = Node(val=0, prev=None, next=None, child=None)
#     # curr_node = dummy_head
#     curr_node = head_node
#     for i in nums:
#         if i:
#             curr_node.next = Node(val=i, prev=curr_node, next=None, child=None)
#         else:
#             count = 0
#             while i is None:
#                 count += 1
#                 curr_node = curr_node.next
#             curr_node.child = create_doubly_linked_list(nums[count:])

def test(head_node, nums):
    for i in nums:
        if i is not None:
            print(i)
        else:
            while i is None:



if __name__ == '__main':
    nums = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12]
