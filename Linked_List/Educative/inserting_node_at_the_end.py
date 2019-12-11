'''
QUESTION -
----------
Given a node pointing to the head of a LL, and a new node 'N', insert 'N' to the end of the LL.
Sample Input: 10-->20-->30-->40-->None
Output: 5-->10-->20-->30-->40-->50-->None

APPROACH -
----------
    1. Create a Node class to initialize attributes - value of node and its next pointer.
    2. Create object nodes to form a linked list.
    3. First node of LL is the head.
    4. Create a new node to be added.
    5. Traverse through the list to find the last node of LL. Make a connection such that the last node points to the new node.
    6. New node 'N' points to None.


    TIME COMPLEXITY - O(1) Inserting in LL is constant time operation.
    SPACE COMPLEXITY - O(1) as resulting LL space is not considered.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def insertAtTheEnd(self, head, N):
        current = head
        while current.next:
            current = current.next
        current.next = N

    def printLinkedList(self, head):
        current = head
        while current.next:
            print(current.value, end = '-->')
            current = current.next
        print(current.value)


if __name__ == '__main__':
    node1 = Node(0)
    node2 = Node(-12)
    node3 = Node(72)
    node4 = Node(100)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    N = Node(-1)

    s = Solution()
    print(s.insertAtTheEnd(node1, N))
    print(s.printLinkedList(node1))
