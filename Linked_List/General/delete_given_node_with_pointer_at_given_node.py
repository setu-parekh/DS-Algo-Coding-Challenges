'''
QUESTION -
----------
Delete a node (except the tail) in singly LL, provided access only to that node i.e the pointer is at the given node instead of head node.
Sample Input: 10 --> 20 --> 30 --> 50 --> 40 and given node = 20
Output: 10 --> 30 --> 50 --> 40

APPROACH -
----------
    1. Modify the value of the given node to be deleted by the value of the next node.
    2. After modifying the value, update the connection : node.next = node.next.next

    TIME COMPLEXITY - O(1) as only node value and link connection was modified.
    SPACE COMPLEXITY - O(1) as resulting LL space is not considered.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def deleteGivenNode(self, node):
        node.value = node.next.value # Modifying the value of the given node equal to the value of the same node.
        node.next = node.next.next # Updating the connections.

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
    s.deleteGivenNode(node4)
    s.printLinkedList(node1)
