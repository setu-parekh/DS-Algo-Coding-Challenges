'''
QUESTION -
----------
https://leetcode.com/problems/symmetric-tree/
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
A given binary tree is symmetric if -
    1. Their two roots have the same value.
    2. The right subtree of each tree is a mirror reflection of the left subtree of the other tree.


APPROACH -
----------
Recursive:
    Base Case:
        1. If both the nodes(left and right) are None, return True
        2. If any one of the nodes(left and right) is None, return False
    Recursion:
        1. check whether nodes are equal in left and right sub-trees, and recursively call (node1.left, node2.right) and (node1.right, node2.left) for mirror check.

    Time Complexity:
    ----------------
    O(N) as we traversed through the entire tree. N is the number of nodes in the tree

    Space Complexity:
    -----------------
    Average - O(logN) as recursive calls made is equal to the height of the tree. Stack is created during recursive calls.
    Worst - O(N) if tree is skewed in either left or right direction.

Iterative:
    1. Declare and initialize a queue = [root,root]
    2. Traverse the tree as breadth first search.
    3. Iterate through the queue till it is not empty:
        - Pop first 2 nodes at a time and compare their value
        - if the values are equal, then append left/right of both nodes alternatively.
        - while popping 2 nodes at a time,
            i) if both is None: do nothing and continue with next 2 nodes.
            ii) if one of them is None: return False as the tree is not symmetrical then.
            iii) if values of both nodes is different, return False as the tree is not symmetrical then.

    Time Complexity:
    ----------------
    O(N) as we traversed through the entire tree. N is the number of nodes in the tree

    Space Complexity:
    -----------------
    O(N) as we created temporary queue which takes space.

'''

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def isSymmetricRecursive(self, root):
        return self.checkMirror(root,root)

    def checkMirror(self,node1,node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False

        return node1.val == node2.val and self.checkMirror(node1.left, node2.right) and self.checkMirror(node1.right, node2.left)

    def isSymmetricIterative(self, root):
        q = [root,root]

        while len(q) != 0:
            node1 = q.pop(0)
            node2 = q.pop(0)

            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            else:
                q.append(node1.left)
                q.append(node2.right)
                q.append(node1.right)
                q.append(node2.left)

        return True

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    s = Solution()
    print(s.isSymmetricIterative(root))
