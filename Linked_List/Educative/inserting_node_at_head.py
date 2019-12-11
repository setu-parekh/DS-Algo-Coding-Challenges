'''
QUESTION -
----------
Given a node pointing to the head of a LL, and a new node 'N', insert 'N' to the start of the LL.
Sample Input: 10-->20-->30-->40-->None
Output: 5-->10-->20-->30-->40-->None

APPROACH -
----------
    1. Create a Node class to initialize attributes - value of node and its next pointer.
    2. Create object nodes to form a linked list.
    3. First node of LL is the head.
    4. Create a new node to be added.
    5. Connect it to the current head.
    6. After making the connection, make that new node as the head node.

    TIME COMPLEXITY - O(1) Inserting in LL is constant time operation.
    SPACE COMPLEXITY - O(1)
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def insertAtTheFront(self, head, N):
        head = node1 # This is the current head node without adding the new node.
        N.next = head # Connecting the new node and current head.
        head = N # Now making that new node as head.
        return head

    def printLinkedList(self,head):
        # Traversing till current.next is not None.
        while head.next:
            print(head.value, end = '-->')
            head = head.next
        print(head.value)


if __name__ == '__main__':
    # Create node objects.
    node1 = Node(0)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)
    # Making the connections for LL.
    node1.next = node2
    node2.next = node3
    node3.next = node4

    N = Node(5) # Creating the new node object which is to be added at the head position.

    s = Solution()
    print(s.insertAtTheFront(node1, N))
    print(s.printLinkedList(N))
