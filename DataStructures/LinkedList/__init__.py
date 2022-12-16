class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_the_end(self, data):
        item = Node(data)
        if self.head is None:
            self.head = self.tail = item
        else:
            self.tail.next = item
            self.tail = item

    def insert_at_the_beginning(self, data):
        item = Node(data)
        if self.head is None:
            self.head = self.tail = item
        else:
            current_head = self.head
            item.next = current_head
            self.head = item

    def insert_and_sort(self, data):
        item = Node(data)
        if self.head is None:
            self.head = self.tail = item
        else:
            if item.data <= self.head.data:
                current_head = self.head
                self.head = item
                item.next = current_head
            else:
                current_node = self.head
                pre_node = self.head
                while True:
                    if item.data > current_node.data:
                        if current_node == self.tail:
                            current_node.next = item
                            self.tail = item
                            break
                        else:
                            pre_node = current_node
                            current_node = current_node.next

                    else:
                        pre_node.next = item
                        item.next = current_node
                        break

    def delete_in_unsorted_list(self, data):
        item = Node(data)
        if self.head is not None:
            current_node = self.head
            pre_node = self.head
            if current_node.data == item.data:
                self.head = current_node.next
                del current_node
            else:
                while True:
                    if current_node.data == item.data:
                        if current_node == self.tail:
                            self.tail = pre_node
                            del current_node
                            break
                        else:
                            pre_node.next = current_node.next
                            del current_node
                            break
                    else:
                        if current_node == self.tail:
                            break
                        else:
                            pre_node = current_node
                            current_node = current_node.next

    def delete_in_sorted_list(self, data):
        item = Node(data)
        current_node = self.head
        pre_node = self.head
        if self.head.data == item.data:
            self.head = current_node.next
            del current_node
        elif self.tail.data < item.data:
            return
        else:
            while True:
                if current_node.data < item.data:
                    pre_node = current_node
                    current_node = current_node.next
                    continue
                elif current_node.data > item.data:
                    break
                else:
                    if current_node == self.tail:
                        if current_node.data == item.data:
                            self.tail = pre_node
                            del current_node
                            break
                        else:
                            break
                    else:
                        pre_node.next = current_node.next
                        del current_node
                        break

    def remove_duplicates_from_sorted_linked_list(self):
        current_node = self.head
        while True:
            if current_node.next is None:
                self.tail = current_node
                break
            if current_node.data == current_node.next.data:
                helper_node = current_node.next
                del current_node.next
                current_node.next = helper_node.next
                del helper_node
            else:
                current_node = current_node.next

    def print_linked_list(self):
        string_linked_list = ""
        current_node = self.head
        while True:
            string_linked_list += str(current_node.data) + "-->"
            current_node = current_node.next
            if current_node == self.tail:
                string_linked_list += str(current_node.data)
                break
        print(string_linked_list)
