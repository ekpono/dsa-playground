# https://leetcode.com/problems/add-two-numbers/description/

# Add Two Numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        setter = ""
        value, value2 = self.crawler(l1, setter), self.crawler(l2, setter)

        summation = map(int, str(int("".join(reversed(str(value)))) + int("".join(reversed(str(value2))))))

        result = None
        for i, val in enumerate(summation):
            newNode = ListNode(val)
            newNode.next = result
            result = newNode
        return result
    
    def crawler(self, node, setter):
        if node is None:
            return setter 
        setter += str(node.val)
        return self.crawler(node.next, setter)
