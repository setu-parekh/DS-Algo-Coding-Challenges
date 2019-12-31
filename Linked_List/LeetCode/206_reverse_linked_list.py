'''
QUESTION -
----------
https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.

Example:
    Input: 1->2->3->4->5->NULL
    Output: 5->4->3->2->1->NULL

APPROACH -
-----------
Iterative:
    1. Initialize 3 pointers: 'Prev' as None, 'current' as head, and 'next' as None.
    2. Traverse through the list till current is not None:
        - Before reversing the connection of current pointer, store the next node in 'next' :
            next = current.next
        - Reverse the connection of current pointer:
            current.next = prev
        - Move prev and current pointers one step forward.
            prev = current
            current = next
    3. After traversal, update the prev pointer as head.

    Time Complexity -
    ---------------
    O(N) as we traversed through whole LL

    Space Complexity -
    ----------------
    O(1) as the resultant reversed list does not use any space.

Recursive:
    Refer - https://www.youtube.com/watch?time_continue=241&v=MRe3UsRadKw&feature=emb_title
    1. We perform the recursion till we reach the last node. Return that last node as head of the reversed LL.
    2. Reverse the pointer connection.

    Time Complexity -
    ---------------
    O(N) as we traversed through whole LL

    Space Complexity -
    ----------------
    - The recursion stack uses the extra space which is O(N).

'''
class Solution:
    def reverseListIterative(self, head: ListNode) -> ListNode:

        prev_pointer = None
        current = head

        while current is not None:
            next = current.next
            current.next = prev_pointer
            prev_pointer = current
            current = next
        head = prev_pointer

        return head

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        # If head or head.next is None, it implies that we reached end of the LL and we have to make the last node as the head node of the reversed LL.
        if head is None or head.next is None:
            return head
        # Recursively call the method till we reach the end of the LL and return the last node as head.
        current = self.reverseList(head.next)
        # These 2 lines will reverse the connection of pointer.
        head.next.next = head
        head.next = None

        return current
