'''
QUESTION -
----------
Given a node pointing to the head of a LL, and an integer value N, delete all nodes of the value N from the list.
Sample Input: 10-->20-->30-->20-->40-->None and N = 20
Output: 10-->30-->40-->None

APPROACH -
----------
    1. Traverse through the list.
    2. If node.value is not equal to the value N, then continue traversing.
    3. If node.value is equal to the value N, then update the connections of previous and next nodes to remove the node with value N.

    TIME COMPLEXITY - O(N) as entire list was traversed.
    SPACE COMPLEXITY - O(1) as resulting LL space is not considered.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def deleteNodeWithValueN(self, head, N):
        current = head

        while current.next:
            # Checking whether the current value is equal to N. If the head = N, the deleting the head and making the 2nd node as head of LL. Updating the connections.
            if current.value == N:
                head = current.next
                current.next = None
                current = head
            # Checking whether current.next is equal to N. If yes, the deleting the current.next node and updating the
            elif current.next.value == N:
                current.next = current.next.next
            else:
                current = current.next

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

    N = 100

    s = Solution()
    s.deleteNodeWithValueN(node1, N)
