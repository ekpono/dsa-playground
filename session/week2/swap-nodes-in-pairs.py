# https://leetcode.com/problems/swap-nodes-in-pairs

"""
first = curr        # first IS curr, same node
second = curr.next

curr.next = first   # you just pointed curr.next back to ITSELF
```

You told node 1 to point at node 1. That's the cycle. `curr.next = first` is identical to `curr.next = curr`.

---

## The Problem With Your Approach

You're trying to swap with only `curr` as your anchor. But swapping two nodes requires **three reference points** not two:

- The node **before** the pair — so you can reconnect the previous group
- The **first** node of the pair
- The **second** node of the pair

Without the node before the pair, you have nowhere to attach the swapped result to the rest of the list.

---

## The Fix — Add A Dummy And A Prev Pointer
```
dummy → [1] → [2] → [3] → [4]
↑      ↑     ↑
prev  first  second
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        first = dummy.next
        second = dummy.next.next


        while first and second:
            nxt = second.next

            second.next = first
            first.next = nxt
            prev.next = second

            prev = first
            first = nxt

            if first:
                second = first.next
            else:
                second = None

        return dummy.next
