'''
QUESTION -
----------
Search for a specific value in a linked list. Return True if present and False if not present.
Sample Input: 10 --> 20 --> 30 --> 50 --> 40 and search node with value = 20
Output: True

APPROACH -
----------
    1. Start from the head node and traverse through the list.
    2. Traverse till we find the node with the desired value.
        - If the desired value is found, then return True.
        - If the desired value is not found after traversing the entire list, then return False.

    TIME COMPLEXITY - O(N) as we traversed through the LL
    SPACE COMPLEXITY - O(1)
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def searchLinkedList(self, head, N):
        current = head

        while current:
            if current.value == N:
                return True
            current = current.next

        return False


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
    print(s.searchLinkedList(node1, -11)) #This will return False
    print(s.searchLinkedList(node1, -12)) #This will return True
