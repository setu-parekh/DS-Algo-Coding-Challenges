'''
QUESTION -
----------
Given a node pointing to the head of a LL, find length of that list.
Sample Input: 10-->20-->30-->40-->None
Output: Length - 4

APPROACH -
----------
    1. Initialize a counter variable to zero.
    2. Traverse through the LL and increment the counter value.
    3. Return the counter value.

    TIME COMPLEXITY - O(N) as we traversed through the entire LL to find the length.
    SPACE COMPLEXITY - O(1) as output length value is not considered as space occupied.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def lengthOfLL(self, head):
        count = 1
        current = head
        while current.next:
            current = current.next
            count += 1
        return count


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
    print(s.lengthOfLL(node1))
