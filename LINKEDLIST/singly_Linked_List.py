# create node
class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

# create linked list

class SLL():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
# insert the newNode in the linkedList
    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            if location == 0:
                newNode.newxt = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

# Traverse the linkedList

    def traverse(self):
        if self.head is None:
            print("there is no linked lisst ")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

# Search an element in linked list

    def search(self, nodeValue):
        if self.head is None:
            print("there is no linked list")
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    print(node.value)
                node = node.next
            return "value is not exist in list"


sll = SLL()
sll.insert(1, 1)
sll.insert(2, 1)
sll.insert(3, 1)
sll.insert(4, 1)
sll.insert(69, 3)
print([node.value for node in sll])

sll.search(69)

