'''
QUESTION -
----------
Insert a new node at head of the Linked List.
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

if __name__ == '__main__':
    # Create node objects.
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)
    # Making the connections for LL.
    node1.next = node2
    node2.next = node3
    node3.next = node4

    new_head_node = Node(5) # Creating the new node object which is to be added at the head position.
    current_node = node1 # This is the current head node without adding the new node.
    new_head_node.next = current_node # Connecting the new node and current head.
    current_node = new_head_node # Now making that new node as head.

    # Traversing through LL till node.next is not None.
    while current_node.next:
        print(current_node.value, end = "-->")
        current_node = current_node.next
    print(current_node.value, "--> None")
