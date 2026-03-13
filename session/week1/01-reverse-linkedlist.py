# https://leetcode.com/problems/reverse-linked-list/submissions/1943171128/

# MENTAL MODEL
"""
1. if head is empty or has only one node, return head
2. initialize pre to None and curr to head
3. while curr is not None:
    a. save next node so that you don't loss pointing to the next node (nxt = curr.next)
    b. reverse the link by pointing the next curr is prev (curr.next = pre)
    c. assign pre to curr (pre = curr)
    d. move curr to rejoin next (curr = nxt)
4. return pre as the new head of the reversed list

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
     def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head

        pre = None
        curr = head

        while curr is not None:
            nxt = curr.next   # save next at the top
            curr.next = pre   # reverse immediately
            pre = curr        # advance pre
            curr = nxt        # advance curr
        return pre
