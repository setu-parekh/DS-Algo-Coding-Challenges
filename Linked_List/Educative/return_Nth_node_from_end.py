'''
QUESTION -
----------
Write a program to return Nth node from end of the Linked List.
Sample Input: 1 --> 2 --> 3 --> 4 --> 5, N = 4
Output:       2

APPROACH (Double Iteration) -
-----------------------------
    1. Iterate to calculate length of the Linked List.
    2. Find the node position from start using length and given Nth node in the input.
    3. Check whether the calculated node position is within the Linked List.
    4. Iterate to the return node at calculated position from head.

    TIME COMPLEXITY: O(N)
    SPACE COMPLEXITY: O(1)

APPROACH (2 Pointers) -
-----------------------
    1. Initialize 2 pointers Nth_node and end_node at head position.
    2. Iterate to bring the end_node at Nth position given in the input while Nth_node pointer is still at head position.
    3. Increment both pointers one step at a time till end_node is not none.
    4. Return Nth_node after traversal.

    TIME COMPLEXITY: O(N)
    SPACE COMPLEXITY: O(1)

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def findNthNodeDoubleIteration(self, head, N):
        length = 1
        count = 1
        current = head

        while current.next:
            current = current.next
            length += 1

        required_node = length - N + 1

        if required_node < 0 or required_node > length:
            return False

        current = head

        while count < required_node:
            current = current.next
            count += 1

        return current.value

    def findNthNodeTwoPointers(self, head, N):
        nth_node = head
        end_node = head
        count = 1

        while count < N:
            end_node = end_node.next
            count += 1

        while end_node.next:
            end_node = end_node.next
            nth_node = nth_node.next

        return nth_node.value

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
    print(s.findNthNodeDoubleIteration(node1, 2))
    print(s.findNthNodeTwoPointers(node1, 2))
