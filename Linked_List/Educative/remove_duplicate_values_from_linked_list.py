'''
QUESTION -
----------
Write a program to remove the duplicate nodes from the linked list. Keep only one of the duplicate and remove the rest.
Sample Input: 1 --> 2 --> 3 --> 2 --> 3 --> 4 --> 5 --> 4 --> 6
Output:       1 --> 2 --> 3 --> 4 --> 5 --> 6

APPROACH (Using Hash method) -
-------------------------------
    1. Create a list to maintain the visited nodes value.
    2. Initialize 2 pointers: prev and current both at head
    3. Traverse through the list:
        - if the node.value is present in the list:
            - prev.next = current.next
            - move current one step forward
            - continue with the loop
        - else:
            - append that node value to the list.
            - make prev as current
            - move current one step forward.

    TIME COMPLEXITY: O(N)
    SPACE COMPLEXITY: O(N)
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def removeDuplicates(self, head):
        visited_node_list = []
        current = head
        prev = head

        if current is not None and current.next is not None: # Checking whether there are atleast 2 elements in LL
            while current is not None:
                if current.value in visited_node_list:
                    prev.next = current.next # If a node is already present in the visited node list, then connect the previous pointer to current.next
                    current = current.next
                    continue # continue checking for the node in the list till new node encountered.

                visited_node_list.append(current.value) # If node not visited previously, then append it to the visited node list.
                prev = current # Moving previous pointer to where the current pointer is before changing the current pointer.
                current = current.next # Moving current pointer one step forward

            self.printLinkedList(head)
        else:
            print("Linked List does not contain sufficient nodes!")

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
    node6 = Node(-12)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    s = Solution()
    s.removeDuplicates(node1)
