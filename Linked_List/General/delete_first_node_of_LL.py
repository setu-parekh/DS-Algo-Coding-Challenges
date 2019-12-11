'''
QUESTION -
----------
Given a node pointing to the head of a LL, delete 1st node of the list.
Sample Input: 10-->20-->30-->40-->None
Output: 20-->30-->40-->50-->None

APPROACH -
----------
    1. Initialize current variable as the present head of LL.
    2. Make the 2nd node of the LL as head.
    3. Point the node at current position to None.

    TIME COMPLEXITY - O(1) because deletion of 1st element is constant time operation.
    SPACE COMPLEXITY - O(1) as resulting LL space is not considered.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def deleteFirstNode(self,head):
        current = head
        head = current.next # Making 2nd node of LL as new head.
        current.next = None # Pointing the original head to None to break the connection.
        return head.value

if __name__ == '__main__':
    node1 = Node(0)
    node2 = Node(-12)
    node3 = Node(72)
    node4 = Node(100)
    node5 = Node(-11)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    s = Solution()
    print(s.deleteFirstNode(node1))
