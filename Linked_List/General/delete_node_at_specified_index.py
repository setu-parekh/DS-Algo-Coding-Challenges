'''
QUESTION -
----------
Given a node pointing to the head of a LL, and an integer value N which is the index of the node in that LL, starting at 1, delete the Nth node of that list.
Sample Input: 10 --> 20 --> 30 --> 50 --> 40 and N = 4
Output: 10 --> 20 --> 30 --> 40

APPROACH -
----------
    1. Initialize the length of LL to 1.
    2. Traverse through the list:
        - If the Nth node = 1, then first point the head towards 2nd element and then update the next pointer of previous head to be removed to None.
        - If any other node than 1:
            - Iterate through N-1 times.
            - At the end of the iteration, update the connections to remove the Nth node.

    TIME COMPLEXITY - O(N) as the list was traversed till N-1.
    SPACE COMPLEXITY - O(1) as resulting LL space is not considered.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def deleteNthNode(self, head, N):
        length = 1
        current = head
        # If removing the head node:
        if N == 1:
            head = current.next
            current.next = None
        # If removing any other node:
        else:
            while length < N-1:
                current = current.next
                length += 1
            current.next = current.next.next

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

    N = 3

    s = Solution()
    s.deleteNthNode(node1, N)
