'''
QUESTION -
----------
https://leetcode.com/problems/diameter-of-binary-tree/
Find diameter of a given binary tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root. NOTE - count number of edges between 2 nodes to find diameter of the tree.

Example -
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
    Diameter for above BT is 5 and the path passes through the root. [2 - 4 - 6 - 9 - 12 - 14]

Example -
                                6
                                |
                         -------------
                        |             |
                        4             9
                        |
                     -------
                    |       |
                    2       5
                    |       |
                  -----    ----
                 |     |  |    |
                 10    14 0    11
                 |             |
               -----         -----
              |     |       |     |
              3     7       9    None

    Diameter for above BT is 6 and path does not pass through the root. [3 - 10 - 2 - 4 - 5 - 11 - 9]

APPROACH -
----------
Recursive:
    Base Case -
        1. Return 0 if the root node is None
    Recursion -
        There will be 3 cases:
            1. Find diameter of BT considering the path passing through the root node.
            2. Find diameter of left sub-tree where path is contained in left sub-tree area (does not pass through the root node).
            3. Find diameter of right sub-tree where path is contained in right sub-tree area (does not pass through the root node).

        - After finding diameter for root, left and right subtrees: compare all 3 diameters and return the max out of them.

        Case 1: Root Diameter
            1. Find the height of left sub-tree.
            2. Find the height of right sub-tree.
            3. Diameter = (left_height + 1) + (right_height + 1). We add 1 to each side to consider the edge between root node and left/right nodes.

        Case 2: Left Diameter
            1. Now recursively consider nodes of left subtree.
            2. Node = root.left
            3. Repeat the steps from Case 1 after hitting base case.

        Case 3: Right Diameter
            1. Now recusively consider nodes of right subtree.
            2. Node = root.right
            3. Repeat steps from Case 1 after hitting base case.

    Time Complexity -
    -----------------
    O(N) as we traversed through entire tree.

    Space Complexity -
    ------------------
    O(N) as a call stack is created during depth first search.

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def height(self,node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        # find diameter of BT considering path through the root node
        rootDiameter = self.height(root.left) + self.height(root.right) + 2 # we add 1 each to left and right heights to consider the edge between the root node and root.left, root node and root.right
        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)

        return max(rootDiameter, leftDiameter, rightDiameter)
        # If instead of adding the edges between the nodes for finding diameter, we are required to consider the number of nodes within the path:
            # return max(rootDiameter, leftDiameter, rightDiameter) + 1 as number of nodes = number of edges + 1.
