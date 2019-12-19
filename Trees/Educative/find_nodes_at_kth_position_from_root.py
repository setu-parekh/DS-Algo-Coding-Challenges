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

Expected output for k = 2: [2,5,8,12]

APPROACH -
----------
Recursive:
    Base Case:
        1. return if node is None.
        2. append the node value if the counter (starting from 0) becomes equals to K after recursive calls.

    1. Recursively call node.left and increment the counter variable during each call.
    2. When counter becomes equal to K, then append that node value to the list and stop the recursion.
    3. Next, recursively call node.right and increment the counter variable during each call.
    4. When counter becomes equal to K, then append that node value to the list and stop iterating.

TIME COMPLEXITY -
-----------------
O(N) as we traversed all nodes till level K.

SPACE COMPLEXITY -
------------------
O(N) as a stack is created during recursive function calls.
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

    # Method to find nodes at Kth position from the root node.
    def findKNodes(self, node, k):
        nodeList = []
        self.findNodesAtPosition(node, k, 0, nodeList)
        return nodeList

    # Helper function for above method recursively calling left and right nodes till the desired K-level is reached.
    def findNodesAtPosition(self,node, k, count, lst):
        if node is None:
            return
        if k == count:
            lst.append(node.value)
        else:
            self.findNodesAtPosition(node.left,k,count+1,lst)
            self.findNodesAtPosition(node.right,k,count+1,lst)



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
    print(bst.findKNodes(root,2))
