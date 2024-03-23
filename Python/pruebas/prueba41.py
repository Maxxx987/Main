


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

            while temp is not None:
                if temp.data == key:
                    break
                prev = temp
                temp = temp.next

            if temp == None:
                return

            prev.next = temp.next
            temp = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Test the linked list
if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert_at_beginning(3)
    linked_list.insert_at_beginning(2)
    linked_list.insert_at_beginning(1)

    print("Linked List:")
    linked_list.print_list()

    linked_list.delete_node(2)

    print("After deleting node with value 2:")
    linked_list.print_list()
