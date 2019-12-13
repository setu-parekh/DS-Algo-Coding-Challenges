'''
QUESTION -
----------
Given two lists, A and B, the union is the list that contains elements or objects that belong to either A, B, or to both.
Sample Input:
    list1: 10->20->80->60
    list2: 15->20->30->60->45
Output: 10->20->80->60->15->30->45

APPROACH -
----------
    1. Traverse through the 1st linked list to reach the tail node.
    2. After reaching tail node, connect tail to head of LL2.
    3. Traverse through the entire combined list and remove the duplicates.
    4. Print the final Linked List.

    TIME COMPLEXITY: O(N)
    SPACE COMPLEXITY: O(1)

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def union(self, head1, head2):
        # If 1st Linked List is empty, then return 2nd Linked List.
        if head1 is None:
            return self.printLinkedList(head2)
        # If 2nd Linked List is empty, then return 1st Linked List.
        elif head2 is None:
            return self.printLinkedList(head1)
        else:
            current = head1 # Starting to traverse from head of 1st LL and reaching tail node.
            while current.next:
                current = current.next
            current.next = head2 # tail node of 1st LL is connected to head node of 2nd LL.

            self.removeDuplicates(head1) # Removing duplicates from the combined list.

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
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(80)
    node4 = Node(60)

    node11 = Node(15)
    node12 = Node(20)
    node13 = Node(30)
    node14 = Node(60)
    node15 = Node(45)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    node11.next = node12
    node12.next = node13
    node13.next = node14
    node14.next = node15

    s = Solution()
    s.union(node1, node11)
