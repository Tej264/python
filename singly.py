class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self,data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            print("Key not found.")
            return

        prev.next = current.next
        current = None

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print("Linked List:")
linked_list.display()

linked_list.delete(2)

print("Linked List after deletion:")
linked_list.display()

linked_list.append(4)
print("after insert list:")
linked_list.display()