class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push_back(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = node  

    def display(self):
        temp = self.head

        while temp:
            print(temp.data,"->", end=" ")
            temp = temp.next
        print(None)

l = LinkedList()
l.push_back(1)
l.push_back(2)
l.push_back(3)
l.push_back(4)
l.push_back(5)

l.display()
