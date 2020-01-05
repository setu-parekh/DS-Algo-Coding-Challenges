'''
QUESTION -
----------
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Assume -  The two numbers do not contain any leading zero, except the number 0 itself.

Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807

APPROACH -
----------
    1. Since it is given to us that both LL are non-empty, we dont have to check for the boundary condition.
    2. As we have to add the nodes of both LL and create a new result LL, we will initialize a new node (sum_result) of the result LL and at the same time save this node to another variable, sum_head so that it can be returned in the end.
    3. Initialize carry = 0
    4. It is not necessary for both LL to be of the same lenghts. So we will have 3 cases:
        - When nodes of l1 and l2 are present.
        - When nodes of l1 present if l1 > l2.
        - When nodes of l2 present if l2> l1.
    5. When l1 and l2 both are present, do:
        - Initially carry will be 0, so sum = l1 + l2 + carry.
        - Result node = sum % 10
        - carry = sum//10
        - Insert result node as the next node of sum_result.
        - Move to next node of l1.
        - Move to next node of l2.
        - Move to next node of sum_result.
    6. When only l1 present, do:
        - sum = l1 + l2 + carry
        - Result node = sum % 10
        - carry = sum//10
        - Insert result node as the next node of sum_result.
        - Move to next node of l1.
        - Move to next node of sum_result.
    7. When only l2 present, do:
        - sum = l1 + l2 + carry
        - Result node = sum % 10
        - carry = sum//10
        - Insert result node as the next node of sum_result.
        - Move to next node of l2.
        - Move to next node of sum_result.
    8. In the end, if carry is still having some value, simply insert that value as the next node to the sum_result LL.
    9. return next node of sum_head as sum_head itself was some dummy node.

    Time Complexity -
    -----------------
    - As we are iterating once through both LLs, time complexity is O(N) where N is the length of the biggest out of l1 and l2.

    Space Complexity -
    ------------------
    - As the result LL does not occupy the extra space, space complexity is O(1).

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_result = ListNode(float('inf')) # Dummy node
        sum_head = sum_result
        carry = 0

        while l1 and l2:
            sum_nodes = l1.val + l2.val + carry
            sum_val = sum_nodes % 10
            carry = sum_nodes//10
            sum_result.next = ListNode(sum_val)
            l1 = l1.next
            l2 = l2.next
            sum_result = sum_result.next

        while l1:
            sum_nodes = l1.val + carry
            sum_val = sum_nodes % 10
            carry = sum_nodes//10
            sum_result.next = ListNode(sum_val)
            l1 = l1.next
            sum_result = sum_result.next

        while l2:
            sum_nodes = l2.val + carry
            sum_val = sum_nodes % 10
            carry = sum_nodes//10
            sum_result.next = ListNode(sum_val)
            l2 = l2.next
            sum_result = sum_result.next

        if carry != 0:
            sum_result.next = ListNode(carry)

        return sum_head.next
