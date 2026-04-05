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

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(None)

    def bubble_sort(self):
        if not self.head:
            return

        while self.head:
            curr = self.head
            swapped = False

            while curr.next:
                if curr.data > curr.next.data:
                    curr.data, curr.next.data = curr.next.data, curr.data
                    swapped = True
                curr = curr.next
            if not swapped:
                break

l = LinkedList()
l.append(5)
l.append(3)
l.append(7)
l.append(2)
l.append(6)
l.append(8)
l.append(4)
l.append(9)

l.display()
l.bubble_sort()
l.display()
