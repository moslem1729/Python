class Node(object):
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_the_end(self, data):
        item = Node(data)
        if self.head is None:
            self.head = item
            self.tail = item
        else:
            item.prev = self.tail
            self.tail.next = item
            self.tail = item

    def insert_at_the_beginning(self, data):
        item = Node(data)
        if self.head is None:
            self.head = item
            self.tail = item
        else:
            item.next = self.head
            self.head.prev = item
            self.head = item

    def insert_and_sort(self, data):
        item = Node(data)
        if self.head is None:
            self.head = item
            self.tail = item
        else:
            if item.data < self.head.data:
                self.head.prev = item
                item.next = self.head
                self.head = item
            else:
                current_node = self.head
                next_node = self.head.next
                while True:
                    if item.data > current_node.data and next_node is None:
                        current_node.next = item
                        item.prev = current_node
                        self.tail = item
                        break
                    elif current_node.data < item.data < next_node.data:
                        current_node.next = item
                        item.prev = current_node
                        item.next = next_node
                        next_node.prev = item
                        break
                    else:
                        current_node = current_node.next
                        next_node = next_node.next

    def print_doubly_linked_list(self):
        current_node = self.head
        doubly_linked_list = ""
        while True:
            if current_node is None:
                break
            else:
                doubly_linked_list += str(current_node.data) + "-->"
                current_node = current_node.next

        print(doubly_linked_list)

    def delete_in_unsorted_list(self, data):
        item = Node(data)
        if item.data == self.head.data:
            current_head = self.head
            self.head.next.prev = None
            del self.head
            self.head = current_head.next
        if item.data == self.tail.data:
            current_tail = self.tail
            self.tail.prev.next = None
            del self.tail
            self.tail = current_tail.prev
        current_node = self.head
        while True:
            if item.data == current_node.data:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                del current_node
                break
            else:
                current_node = current_node.next
            if current_node is None:
                break

    def delete_in_sorted_list(self, data):
        item = Node(data)
        current_node = self.head
        next_node = self.head.next
        if current_node.data == item.data:
            self.head = current_node.next
            self.head.prev = None
            del current_node
        else:
            while True:
                if next_node is None:
                    if current_node.data == item.data:
                        self.tail = current_node.prev
                        self.tail.next = None
                        del current_node
                        break
                    else:
                        break
                else:
                    if current_node.data == item.data:
                        current_node.prev.next = next_node
                        next_node.prev = current_node.prev
                        del current_node
                        break
                    elif item.data < next_node.data:
                        break
                    else:
                        current_node = next_node
                        next_node = current_node.next


doubly_linked_list = DoublyLinkedList()
doubly_linked_list.insert_and_sort(4)
doubly_linked_list.insert_and_sort(3)
doubly_linked_list.insert_and_sort(2)
doubly_linked_list.insert_and_sort(1)
doubly_linked_list.insert_and_sort(9)
doubly_linked_list.insert_and_sort(7)
doubly_linked_list.insert_and_sort(0)
doubly_linked_list.insert_and_sort(12)
doubly_linked_list.insert_and_sort(-14)
doubly_linked_list.delete_in_sorted_list(12)
doubly_linked_list.print_doubly_linked_list()
print(doubly_linked_list.tail.prev.data)
print(doubly_linked_list.tail.prev.data)
