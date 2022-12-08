class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.head.next is None:
            self.tail = self.head

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return
        self.tail.next = new_node
        self.tail = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" --> ")
            temp = temp.next
        print("None")


random_node = LinkedList()
# random_node.prepend(4)
random_node.append(2)
random_node.append(4)
random_node.print_list()
print(random_node.head.value)
random_node.prepend(9)
print(random_node.head.value)
random_node.print_list()
