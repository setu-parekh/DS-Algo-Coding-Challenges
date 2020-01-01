'''
QUESTION -
----------
Given a node pointing to the head of a LL, find middle element of that list.
Sample Input (Even nodes): 10-->20-->30-->40-->None
Output: Middle node = 30 (There are 2 mids: 20 and 30. select 2nd middle node.)
Sample Input (Odd nodes): 10-->20-->30-->40--->50-->None
Output: Middle node = 30 (There is only 1 mid as there are odd number of nodes.)

APPROACH:
---------
1. Define a method to find length of the LL by traversing through the list.
2. Define another method to find the middle node:
    - Divide the length by 2.
    - Traverse through the list till (length/2 + 1) node.
    - Return the last node after completing the half traversal.

    TIME COMPLEXITY - O(N)
    SPACE COMPLEXITY - O(1)
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:

    def middleNode(self, head):
        fast = head
        slow = head

        while fast.next:
            fast = fast.next
            fast = fast.next
            slow = slow.next
        return slow.value


if __name__ == '__main__':
    node1 = Node(0)
    node2 = Node(-12)
    node3 = Node(72)
    node4 = Node(100)
    node5 = Node(-11)
    node6 = Node(0)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    s = Solution()
    print(s.middleNode(node1))
