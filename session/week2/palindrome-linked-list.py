# https://leetcode.com/problems/palindrome-linked-list/

"""
MENTAL MODEL
1. Use fast and slow pointer to find the middle of the linked list
2. Reverse the second half of the linked list starting from the slow pointer
3. Compare the first half and the reversed second half of the linked list
    a. Initialize pre to None and curr to slow
    b. While curr is not None:
        i. Save the next node (nxt = curr.next)
        ii. Reverse the link (curr.next = pre)
        iii. Move pre to curr (pre = curr)
        iv. Move curr to nxt (curr = nxt)
4. After reversing the second half, pre will be the head of the reversed second half, so we can compare it with the first half starting from head
5. While pre is not None:
    a. If pre.val is not equal to head.val, return False
    b. Move pre to pre.next
    c. Move head to head.next
6. If the loop ends, it means all nodes are matched, return True
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        pre = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt

        while pre:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next


        return True

