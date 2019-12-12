'''
QUESTION -
----------
Write a program to detect loop in a LL. Return True if present and False if not present.
Sample Input: 10 --> 20 --> 30 --> 50
                      |             |
                       -------------
Output: True

APPROACH (Using Hashing Technique) -
-------------------------------------
    1. Start from the head node and traverse through the list.
    2. Add each traversed node to the node_list.
    3. During iteration we check whether the node is present in the node list or not.
        - If present: cycle detected.

    TIME COMPLEXITY -
        Average Case: O(N) as we traversed through the LL and lookup for a node in list on an average                    takes O(1).
        Worst Case: O(N^2) as we traversed through the LL and lookup for a node in list may take O(N) time.

    SPACE COMPLEXITY - O(N) as a temporary node_list was created.

APPROACH (Using fast and slow iterators - Flyod's cycle finding Algorithm) -
-----------------------------------------------------------------------------
    1. Initialize the slow and fast pointers. Slow moves one step at a time and fast moves 2 steps at a time.
    2. Iterate till fast.next.next.
    3. If the cycle is present, both the pointers will meet at same node at some point of time.

    TIME COMPLEXITY - O(N). It is same as that of hashing technique. But in terms of speed, this method is                         twice as fast than hashing.
    SPACE COMPLEXITY - O(1)

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def detectLoopUsingHashing(self, head):
        node_list = [] # Node list to store the traversed nodes of the LL.
        current = head

        while current:
            if current in node_list: # While LL traversal, if some node is already present in the node list, that indicates cycle.
                return True
            node_list.append(current)
            current = current.next

        return False

    def detectLoopUsingTwoPointers(self, head):
        slow = head # Moves 1 step at a time.
        fast = head # Moves 2 steps at a time.
        while slow and fast and fast.next: # Writing fast.next.next will error out in while loop.
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # This happens when cycle is present in LL.
                return True
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
    node5.next = node1

    s = Solution()
    print(s.detectLoopUsingHashing(node1))
    print(s.detectLoopUsingTwoPointers(node1))
