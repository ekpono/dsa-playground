class Node:
        def __init__(self, data):
                self.next = None
                self.data = data
        

node1 = Node(10)
node2 = Node(40)
node3 = Node(42)
node4 = Node(100)
node5 = Node(80)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def loopAndPrint(head):
        while head:
                print('>>>', head.data)
                head = head.next



def findTheLowest(head):
        currentNode = head
        lowestValue = currentNode.data
        while currentNode:
                if currentNode.data < lowestValue :
                        lowestValue = currentNode.data
                currentNode = currentNode.next
        # print(lowestValue)

def deleteSpecificNode(head, nodeToDelete):
        print(head, nodeToDelete)
        print(head == nodeToDelete)
        if head == nodeToDelete:
                return head.next
        
        currentNode = head
        while currentNode.next and currentNode.next != nodeToDelete:
                currentNode = currentNode.next
        
        if currentNode.next is None:
                return head
        
        currentNode.next = currentNode.next.next

        return head



def insertNodeAtPosition(head, newNode, position):
        if position == 1:
                newNode.next = head
                return newNode
        
        currentNode = head
        for _ in range(position - 2):
                if currentNode is None:
                        break

                currentNode = currentNode.next

        newNode.next = currentNode.next
        currentNode.next = newNode

        return head


findTheLowest(node1)

newNode = Node(201)
position = 2
expr = insertNodeAtPosition(node1, newNode, position)

result = deleteSpecificNode(node1, node1)
loopAndPrint(expr)