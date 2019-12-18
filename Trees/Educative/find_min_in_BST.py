'''
QUESTION -
----------
Given the root of BST, write a function to find minimum value in that tree.
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

APPROACH -
-----------
    Edge Cases:
        1. if root node is none: return -1
        2. if only root node is present: minimum value is the root node itself
    1. Move node.left till the end of the tree is reached.
    2. When node.left is None, then that node value is the minimum value of the given tree.

TIME COMPLEXITY -
-----------------
O(NlogN)

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

    def findMin(self, node):
        if node is None: # Edge Case 1
            return -1

        if node.left is None and node.right is None: # Edge Case 2
            return node.value

        current = node

        while current.left:
            current = current.left

        return current.value


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
    print("Minimum value is {}".format(bst.findMin(root)))
