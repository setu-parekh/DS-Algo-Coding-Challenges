'''
QUESTION -
----------

Sample Input: 1 --> 2 --> 3 --> 4 --> 5
Output:       2

APPROACH -
----------


    TIME COMPLEXITY: O(N)
    SPACE COMPLEXITY: O(1)

APPROACH -
----------

    TIME COMPLEXITY: O(N)
    SPACE COMPLEXITY: O(1)

'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def intersectionByModifyingLL(self, head1, head2):
        dict = {}
        current = head1

        while current:
            if current.value not in dict:
                dict[current.value] = 1
            else:
                dict[current.value] += 1
            current = current.next

        new_head = head2
        current = head2
        prev = new_head

        while current:
            if dict.get(current.value) is None:
                current = current.next
                new_head.next = None
                new_head = current
                continue
            else:
                if dict.get(current.next.value) is None:
                    current = current.next.next
                    prev.next = current
                    prev = current
                else:
                    current = current.next
                    prev.next = current
                    prev = current

        self.printLinkedList(new_head)

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
    s.intersectionByModifyingLL(node1, node11)
