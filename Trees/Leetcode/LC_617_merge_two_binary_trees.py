'''
QUESTION -
----------
https://leetcode.com/problems/merge-two-binary-trees/
Merge two given binary trees
    - if two nodes overlap, then sum node values up as the new value of the merged node.
    - Otherwise, the NOT null node will be used as the node of new tree.

APPROACH -
----------
Recursive (Modifying treeOne in place):
    Base Case -
        1. If root1 is None: return root2
        2. If root2 is None: return root1
        3. If root1 and root2 is None: return
    Recursion -
        1. treeOneNode = treeOneNode + treeTwoNode
        2. Recursively call treeOneNode.left
        3. Recursively call treeTwoNode.right
        4. return treeOneNode in the end.

    Time Complexity -
    -----------------
    O(N) as we traversed through the entire tree.

    Space Complexity -
    ------------------
    O(N) as a call stack is created.

Iterative:
    1. First, initialize a stack with pair of roots of both trees.
    2. Check following edge cases:
        - if node1 is None: return node2
        - if node2 is None: return node1
        - if node1 and node2 both is None: return -1
    3. Iterate till the stack is not empty:
        - pop the pair of nodes of both trees.
        - modify the node1 of Tree1 as the summation of node1 and node2.
        - if node1.left is None and node2.left is not None:
        use node2.left as node1.left
        - if node1.right is None and node2.right is not None:
        use node2.right as node1.right
        - if left of node1 and node2 is present: append the pair to the stack.
        if right of node1 and node2 is present: append the pair to the stack.
    4. return node1 of Tree1.

    Time Complexity -
    -----------------
    O(N) as we traversed through the entire tree.

    Space Complexity -
    ------------------
    O(N) as a temp stack is created.


'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTreesRecursive(self, t1: TreeNode, t2: TreeNode):
        # Base Case:
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        elif t1 is None and t2 is None:
            return None
        # Adding corresponding node values of both trees and assigning the added value to tree1 node.
        t1.val = t1.val + t2.val
        t1.left = self.mergeTreesRecursive(t1.left, t2.left)
        t1.right = self.mergeTreesRecursive(t1.right, t2.right)
        return t1

    def mergeTreesIterative(self, t1: TreeNode, t2: TreeNode):
        s = [(t1, t2)]
        if not t1:
            return t2
        elif not t2:
            return t1
        elif not t1 and not t2:
            return -1
        else:
            while len(s) != 0:
                (node1, node2) = s.pop()
                node1.val = node1.val + node2.val
                if node1.left and node2.left:
                    s.append((node1.left, node2.left))
                if node1.right and node2.right:
                    s.append((node1.right, node2.right))
                if not node1.left and node2.left:
                    node1.left = node2.left
                if not node1.right and node2.right:
                    node1.right = node2.right

            return t1
