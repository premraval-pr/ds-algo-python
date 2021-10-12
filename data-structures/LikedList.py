class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.numberOfNodes = 0

    # This is the reason we prefer LinkedList, adding at start is simple / O(1)
    def insert_start(self, data):

        self.numberOfNodes += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Insert at end has traversal to the end / O(N)
    def insert_end(self, data):

        self.numberOfNodes += 1
        new_node = Node(data)

        node = self.head

        while node.next is not None:
            node = node.next

        node.next = new_node

    # O(1)
    def size(self):
        return self.numberOfNodes

    # O(N)
    def traverse(self):

        node = self.head

        while node is not None:
            print(node.data)
            node = node.next

    def remove(self, data):

        if self.head is None:
            return

        node = self.head
        prev_node = None

        while node is not None and node.data != data:
            prev_node = node
            node = node.next

        # search miss
        if node is None:
            return

        self.numberOfNodes -= 1
        if prev_node is None:
            self.head = node.next
        else:
            prev_node.next = node.next


ll = LinkedList()

ll.insert_start(4)
ll.insert_start(3)
ll.insert_start(7)
ll.insert_end(10)
ll.insert_end(100)
ll.insert_end(1000)
ll.traverse()
print("-------")
ll.remove(3000)
ll.remove(10)
ll.traverse()
print("LL size = " + str(ll.size()))
