'''
QUESTION -
----------
Given a node pointing to the head of a LL, delete 1st node of the list.
Sample Input: 10-->20-->30-->40-->None
Output: 20-->30-->40-->50-->None

APPROACH -
----------
    1. Initialize 2 pointers i and j for traversing the LL.
        - i points to head.
        - j points to head.next
    2. Traverse LL untill j.next is not None.
    3. Once the end of the list is reached, point i to None which will break the connection between i and j.
    4. Return i.value.

    TIME COMPLEXITY - O(N) as entire list was traversed.
    SPACE COMPLEXITY - O(1) as resulting LL space is not considered.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def deleteLastNode(self,head):
        # i,j are 2 pointers pointing to 1st Node and 2nd Node respectively.
        i = head
        j = head.next
        while j.next:
            i = i.next
            j = j.next
        i.next = None
        return i.value

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
    print(s.deleteLastNode(node1))
