'''
QUESTION -
----------
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
    Input: 1->2->4 and 1->3->4
    Output: 1->1->2->3->4->4

APPROACH -
----------
    1) Declare a false result node. Store the same node in a separate variable (ex: current) which can be used at the end for returning from function.
    2) Iterate over both the given lists simultaneously until currently pointed elements of both lists are not None.
        2.1) Compare the current elements of both the lists. Make result.next = smallest among the current elements.
        2.2) Increment the smaller element list to point to it's next.
        2.3) Increment result to point to it's next.
    3) After the above iteration, one of the two lists must be completely traversed.
        3.1) Check which list is still not completely traversed. Just append that list as result.next (since the given lists are already sorted)
    4) Return (see point 1) result_head.next as head of the merged list.

    Time Complexity -
    -----------------
    Since we are iterating both the linked lists of length M and N, time complexity is O(M+N).

    Space Complexity -
    ------------------
    O(1) as space taken by result LL is not considered as extra space.

'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        result_node = ListNode(float('-inf'))
        current = result_node

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1:
            current.next = l1
        if l2:
            current.next = l2

        return result_node.next
