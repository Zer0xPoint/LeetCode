class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        node.next = self.head
        node.prev = None
        self.head = node

        next_node = self.head.next
        if next_node:
            next_node.prev = node

        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        node = Node(val)
        curr = self.head
        if curr is None:
            self.head = node
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = node
            node.next = None
            node.prev = curr

        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            curr.next = node
            node.prev = curr

            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = curr.next
            curr.prev = None
        else:
            for i in range(index):
                curr = curr.next
            if curr is None:
                print('1')
            prev_node = curr.prev
            next_node = curr.next
            if prev_node:
                prev_node.next = next_node
            if next_node:
                next_node.prev = prev_node

        self.size -= 1

    def traverse_linked_list(self, linked_list_head):
        # head_node = linked_list_head
        node = self.head
        while node:
            print(node.val)
            node = node.next


if __name__ == "__main__":
    myLinkedList = MyLinkedList()
    # ["MyLinkedList", "addAtHead", "addAtHead", "addAtHead", "addAtIndex", "deleteAtIndex", "addAtHead", "addAtTail",
    #  "get", "addAtHead", "addAtIndex", "addAtHead"]
    # [[], [7], [2], [1], [3, 0], [2], [6], [4], [4], [4], [5, 0], [6]]
    operations = ["MyLinkedList", "addAtHead", "addAtTail", "addAtTail", "addAtTail", "addAtTail", "addAtTail",
                  "addAtTail",
                  "deleteAtIndex", "addAtHead", "addAtHead", "get", "addAtTail", "addAtHead", "get", "addAtTail",
                  "addAtIndex",
                  "addAtTail", "addAtHead", "addAtHead", "addAtHead", "get", "addAtIndex", "addAtHead", "get",
                  "addAtHead",
                  "deleteAtIndex", "addAtHead", "addAtTail", "addAtTail", "addAtIndex", "addAtTail", "addAtHead", "get",
                  "addAtTail",
                  "deleteAtIndex", "addAtIndex", "deleteAtIndex", "addAtHead", "addAtTail", "addAtHead", "addAtHead",
                  "addAtTail",
                  "addAtTail", "get", "get", "addAtHead", "addAtTail", "addAtTail", "addAtTail", "addAtIndex", "get",
                  "addAtHead",
                  "addAtIndex", "addAtHead", "addAtTail", "addAtTail", "addAtIndex", "deleteAtIndex", "addAtIndex",
                  "addAtHead",
                  "addAtHead", "deleteAtIndex", "addAtTail", "deleteAtIndex", "addAtIndex", "addAtTail", "addAtHead",
                  "get",
                  "addAtIndex", "addAtTail", "addAtHead", "addAtHead", "addAtHead", "addAtHead", "addAtHead",
                  "addAtHead",
                  "deleteAtIndex", "get", "get", "addAtHead", "get", "addAtTail", "addAtTail", "addAtIndex",
                  "addAtIndex",
                  "addAtHead", "addAtTail", "addAtTail", "get", "addAtIndex", "addAtHead", "deleteAtIndex", "addAtTail",
                  "get",
                  "addAtHead", "get", "addAtHead", "deleteAtIndex", "get", "addAtTail", "addAtTail"]
    vals = [[], [38], [66], [61], [76], [26], [37], [8], [5], [4], [45], [4], [85], [37], [5], [93], [10, 23], [21],
            [52],
            [15], [47], [12], [6, 24], [64], [4], [31], [6], [40], [17], [15], [19, 2], [11], [86], [17], [55], [15],
            [14, 95],
            [22], [66], [95], [8], [47], [23], [39], [30], [27], [0], [99], [45], [4], [9, 11], [6], [81], [18, 32],
            [20],
            [13], [42], [37, 91], [36], [10, 37], [96], [57], [20], [89], [18], [41, 5], [23], [75], [7], [25, 51],
            [48], [46],
            [29], [85], [82], [6], [38], [14], [1], [12], [42], [42], [83], [13], [14, 20], [17, 34], [36], [58], [2],
            [38],
            [33, 59], [37], [15], [64], [56], [0], [40], [92], [63], [35], [62], [32]]
    for i in range(1, len(operations)):
        if operations[i] == "addAtHead":
            myLinkedList.addAtHead(vals[i][0])
        elif operations[i] == "addAtTail":
            myLinkedList.addAtTail(vals[i][0])
        elif operations[i] == "addAtIndex":
            index, val = vals[i]
            myLinkedList.addAtIndex(index, val)
        elif operations[i] == "deleteAtIndex":
            myLinkedList.deleteAtIndex(vals[i][0])
        elif operations[i] == "get":
            myLinkedList.get(vals[i][0])


