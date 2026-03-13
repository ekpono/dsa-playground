# Adi

class Node:
        def __init__(self, data):
                self.data = data
                self.head = None
                self.tail = None

node1 = Node(1)
node2 = Node(23)
node3 = Node(42)
node4 = Node(55)
node5 = Node(24)

node1.tail = node2

node2.head = node1
node2.tail = node3

node3.head = node2
node3.tail = node4

node4.head = node3
node4.tail = node5

node5.head = node4


currentHead = node1

# Traverse forward
while currentHead:
        print('.>>>><<<<', currentHead.data)
        currentHead = currentHead.tail

print('I have missed you sin')
currentHead = node5
# Traverse backward
while currentHead:
        print('.>>>><<<<', currentHead.data)
        currentHead = currentHead.head


