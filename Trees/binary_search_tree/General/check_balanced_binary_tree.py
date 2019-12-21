'''
QUESTION -
----------
Given the root to a Binary Search Tree, write a function to find the height of the tree.

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

Expected output: 3

APPROACH -
----------
Recursive:
    Base Case:
        1. if node is none: return -1
    Recursion Case:
        1. Recursively call node.left and node.right simultaneously till base case is hit.
        2. Find max out of node.left and node.right.
        3. Add 1 to the max value and return

TIME COMPLEXITY -
-----------------
O(N) as all nodes were visited.

SPACE COMPLEXITY -
------------------
Unbalanced Tree: O(N)
Balanced Tree: O(logN)
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

    def isBalanced(self,node):
        if node is None:
            return 0

        leftHeight = self.isBalanced(node.left)
        # If left sub-tree is not balanced then this tree is also not balanced.
        if leftHeight == -1:
            return -1

        rightHeight = self.isBalanced(node.right)
        # If right sub-tree is not balanced then this tree is also not balanced.
        if rightHeight == -1:
            return -1
        # If difference in heights is greater than 1, then tree is not balanced.
        if abs(leftHeight - rightHeight) > 1:
            return -1
        # if tree is balanced, return height (root level = 1)
        return 1 + max(leftHeight, rightHeight)


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
    bst.insertNode(16)
    # print(bst.findHeight(root))
    print(bst.isBalanced(root))
