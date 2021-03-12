class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy_head = ListNode(0)
        self.dummy_tail = ListNode(0)
        self.dummy_tail.prev = self.dummy_head
        self.dummy_head.next = self.dummy_tail
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        curr_node = self.dummy_head.next
        for __ in range(index):
            curr_node = curr_node.next
        return curr_node.val

    def addAtHead(self, val):
        node = ListNode(val)
        node.next = self.dummy_head.next
        node.prev = self.dummy_head
        self.dummy_head.next.prev = node
        self.dummy_head.next = node

        self.size += 1

    def addAtTail(self, val):
        node = ListNode(val)
        node.prev = self.dummy_tail.prev
        node.next = self.dummy_tail
        self.dummy_tail.prev.next = node
        self.dummy_tail.prev = node

        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            curr_node = self.dummy_head.next
            for __ in range(index - 1):
                curr_node = curr_node.next
            node = ListNode(val)
            node.next = curr_node.next
            node.prev = curr_node
            curr_node.next.prev = node
            curr_node.next = node

            self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        curr_node = self.dummy_head
        for __ in range(index):
            curr_node = curr_node.next
        curr_node.next.next.prev = curr_node
        curr_node.next = curr_node.next.next

        self.size -= 1

    def traverse_linked_list(self):
        node = self.dummy_head.next
        linked_list = []
        for __ in range(self.size):
            linked_list.append(node.val)
            node = node.next
        print(linked_list)

    def traverse_linked_list_backwards(self):
        node = self.dummy_tail.prev
        backwards_linked_list = []
        for __ in range(self.size):
            backwards_linked_list.append(node.val)
            node = node.prev
        print(backwards_linked_list)


# if __name__ == "__main__":
#     myLinkedList = MyLinkedList()
#     operations = ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
#     vals = [[], [1], [3], [1, 2], [4], [1], [1]]
#     for i in range(1, len(operations)):
#         if operations[i] == "addAtHead":
#             myLinkedList.addAtHead(vals[i][0])
#         elif operations[i] == "addAtTail":
#             myLinkedList.addAtTail(vals[i][0])
#         elif operations[i] == "addAtIndex":
#             index, val = vals[i]
#             myLinkedList.addAtIndex(index, val)
#         elif operations[i] == "deleteAtIndex":
#             myLinkedList.deleteAtIndex(vals[i][0])
#         elif operations[i] == "get":
#             myLinkedList.get(vals[i][0])
#         myLinkedList.traverse_linked_list()
#         myLinkedList.traverse_linked_list_backwards()
