'''
QUESTION -
----------
Given the root to a Binary Search Tree and a number "k" write a function to find the kth maximum value in the tree.
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

Expected output for k = 3: 10

APPROACH -
----------
Iterative:

    Edge Case:
        1. if node is none: return
        2. if K is not between 0 to length of the list.
    1. Perform inorder traversal and store it in a list.
    2. Write a method to find the Kth max value of BST and call the inOrder traversal method to obtain the list in ascending order.
    3. Return list[-k]

Recursive:

    Base Case:
        1. if node is none: return
        2. if counter value >= K: return
    Recursion:
        1. Initialize counter value to 0.
        2. Recursively call the method with node = node.right. Right most element in BST will have maximum node value.
        3. Increment the counter once the base case is hit and recursion of particular node ends.
            - if counter = K, return that node value.
            - if counter < K, continue with next recursion
        4. Next, recursively call the method with node = node.left. When recursion ends upon hitting the base case, then again increment the counter and compare it with K.


TIME COMPLEXITY -
-----------------
Iterative:
    Best/Average/Worst - O(N) as while performing in-order traversal, we visited all the nodes.
Recursive:
    Best/Average - O(logN)
    Worst - O(N) if BST is skewed.

SPACE COMPLEXITY -
------------------
Iterative:
    O(N) as temporary list was created to store the node values in ascending order after in-order traversal.
Recursive:
    O(N) as temporary stack is created while recursive function calls.

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

    def inOrderRecursive(self,node,lst):
        if node is None:
            return
        else:
            self.inOrderRecursive(node.left, lst)
            lst.append(node.value)
            self.inOrderRecursive(node.right, lst)


    def findKthMax(self,node, k):
        lst = []
        self.inOrderRecursive(node,lst)
        if k > 0 and k < len(lst): # Edge Case 2
            return lst[-k]
        else:
            return

    def findKthMaxRecursive(self,node,k,count):
        # Base Case:
        if node is None:
            return
        if count[0] >= k:
            return
        # Calling the method recursively
        self.findKthMaxRecursive(node.right,k,count)
        count[0] = count[0] + 1
        if count[0] == k:
            print("Kth largest element is {}".format(node.value))
            return
        else:
            self.findKthMaxRecursive(node.left,k,count)


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
    print(bst.findKthMax(root, 3))
    print(bst.findKthMaxRecursive(root, 3, [0]))
