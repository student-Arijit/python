# Represents an individual node in the singly linked list
class Node:
    def __init__(self, data):
        self.data = data  # Stores the data value of the node
        self.next = None  # Pointer to the next node in the list (initialized to None)


# Manages the linked list operations
class LinkedList:
    def __init__(self):
        self.head = None  # Pointer to the first node in the list (initially empty)

    # Appends a new node with the given data to the end of the list
    def push_back(self, data):
        node = Node(data)  # Create a new node instance

        # Case 1: If the list is empty, make the new node the head
        if self.head is None:
            self.head = node
            return

        # Case 2: Traverse to the end of the list
        temp = self.head
        while temp.next:  # Loop until temp reaches the last node
            temp = temp.next

        # Link the last node to the new node
        temp.next = node  

    # Prints the linked list elements in sequence
    def display(self):
        temp = self.head

        # Traverse through every node in the list
        while temp:
            print(temp.data, "->", end=" ")  # Print current node's data
            temp = temp.next                 # Move pointer to the next node
            
        print(None)  # Output None at the end to signify the end of the list


# --- Execution Example ---

# Initialize a new linked list object
l = LinkedList()

# Append elements 1 through 5 to the list
l.push_back(1)
l.push_back(2)
l.push_back(3)
l.push_back(4)
l.push_back(5)

# Display the linked list structure (Output: 1 -> 2 -> 3 -> 4 -> 5 -> None)
l.display()
