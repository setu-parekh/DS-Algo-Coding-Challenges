'''
QUESTION -
----------
Write a program to reverse a given linked list.
Sample Input: 10 --> 20 --> 30 --> 50 --> 40
Output: 40 --> 50 --> 30 --> 20 --> 10

APPROACH -
----------
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

    TIME COMPLEXITY - O(N)
    SPACE COMPLEXITY - O(1)
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def reverseLinkedList(self, head):
        prev_pointer = None
        current = head

        while current is not None:
            next = current.next
            current.next = prev_pointer
            prev_pointer = current
            current = next
        head = prev_pointer

        self.printLinkedList(head)

    def printLinkedList(self, head):
        current = head
        ll_nodes = []

        while current:
            ll_nodes.append(str(current.value))
            current = current.next

        print(' --> '.join(ll_nodes))


if __name__ == '__main__':
    node1 = Node(0)
    node2 = Node(-12)
    node3 = Node(72)
    node4 = Node(100)
    node5 = Node(72)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    s = Solution()
    s.reverseLinkedList(node1)
