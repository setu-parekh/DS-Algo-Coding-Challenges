'''
QUESTION -
----------
Given the root to a Binary Search Tree and a node value "k" write a function to find the ancestors of the given node.

                6
                |
          -------------
         |             |
         4             9
         |             |
      -------       -------
     |       |     |       |
     2       5     8       12
                           |
                        -------
                       |       |
                       10      14

Expected output for k = 10: [12,9,6]

APPROACH -
----------
Iterative:

    Edge Case:
        1. check is root itself is None

    1. Set current to the given input node which is root of the BST in this case.
    2. Initialize an empty list to store the visited nodes while iterating.
    3. Iterate through the tree till current is not None.
        - if k = current.value: return reversed list
        - if k < current.value: append that value and move left
        - if k > current.value: append that value and move right
    4. If k value not found after completion of iteration, return empty list.

TIME COMPLEXITY -
-----------------
O(logN) as only the path of root node to the node = k value is traced

SPACE COMPLEXITY -
------------------
O(1)

'''
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    def insertNode(self, value):
        newNode = Node(value)

        if self.root is None:
            self.root = newNode

        else:
            current = self.root
            while True:
                if value <= current.value:
                    if current.left is None:
                        current.left = newNode
                        break
                    else:
                        current = current.left
                elif value > current.value:
                    if current.right is None:
                        current.right = newNode
                        break
                    else:
                        current = current.right

    def findAncestorsIterative(self, node, k):
        visited = []
        current = node

        if current == None: #Edge Case 1
            return -1

        while current is not None:
            if current.value == k:
                return visited[::-1]

            else:
                if k < current.value:
                    visited.append(current.value)
                    current = current.left
                elif k > current.value:
                    visited.append(current.value)
                    current = current.right

        return []


if __name__ == '__main__':
    root = Node(6)
    bst = BinarySearchTree(root)
    bst.insertNode(4)
    bst.insertNode(2)
    bst.insertNode(5)
    bst.insertNode(9)
    bst.insertNode(12)
    bst.insertNode(8)
    bst.insertNode(10)
    bst.insertNode(14)
    print(bst.findAncestorsIterative(root,14))
