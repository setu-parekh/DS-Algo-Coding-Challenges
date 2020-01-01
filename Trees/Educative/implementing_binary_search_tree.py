'''
QUESTION -
----------
Implement a Binary Search Tree(BST)

APPROACH -
----------
    1. Create a class TreeNode to define various method:
        a. Initialize left and right node of a parent node to None
        b. insertLeft():
            - create a node for a given value as the object of class TreeNode.
            - If the left side of the parent node is empty:
                - insert node to the left.
            - If the left side of the parent node is not empty:
                - Make the existing left sub-tree of the parent node as left sub-tree of the new node to be inserted.
                - insert the new node to the left of the parent node.
        c. insertRight():
            - create a node for a given value as the object of class TreeNode.
            - If the right side of the parent node is empty:
                - insert node to the right.
            - If the right side of the parent node is not empty:
                - Make the existing right sub-tree of the parent node as right sub-tree of the new node to be inserted.
                - insert the new node to the right of the parent node.

    2. Create class BinarySearchTree to perform operation on BST:
        a. Initialize a root node.
        b. insertNode():
            - create a new node for a given value as the object of class TreeNode
            - If there is no root:
                - assign new node to the root.
            - If the root node is already present:
                - if the given value to be inserted is less than the root node:
                    - check left node
                    - repeat checking left node till end is reached.
                    - once end is reached, insert the new node.
                - if the given value to be inserted is greater than the root node:
                    - check right node
                    - repeat checking right node till end is reached.
                    - once end is reached, insert the new node.
        c. searchNode():
            - if there is no root node, then return -1
            - if root node is present, then initialize current as the root node and parent node as None (There is no parent for the root node)
            - Iterate till the end of the tree on either side:
                Case 1: value = root node
                 - return current and parent.
                Case 2: value < current
                 - make current as the parent and move current to left.
                Case 3: value > current
                 - make current as the parent and move current to right.
                Case 4: no match found
                 - return None, None

        d. removeNode():
            - obtain the node to be removed and its parent by calling searchNode() method.
            - if the node is none(not found in the tree during search operation): return False
            - if the node doesnot have left and right child nodes:
                - if node is root node: root node = None
                - if node is on left of parent: parent.left = None
                - if node is on right of parent: parent.right = None
            - if the node has either of left or right node:
                - if node is root node:
                    - if node.left exists: node.value = node.left.value
                    - if node.right exists: node.value = node.right.value
                - if node.left exists:
                    - if node on left side of parent: node_parent.left = node.left
                    - if node on right side of parent: node_parent.right = node.left
                - if node.right exists:
                    - if node on left side of parent: node_parent.left = node.right
                    - if node on right side of parent: node_parent.right = node.right
            if the node has both left and right node:
                - find minimum node(successor) of the right sub tree of the node to be removed.
                - if node is root node:
                    - update the node value to the successor value
                    - if the right subtree of the successor node exists:
                        - move it onto the left side of successor parent node.
                - if node to be removed is on left side of its parent node:
                    - move the successor node onto the left of node parent, thus replacing the node to be removed.
                    - if there is a right subtree to the successor:
                        - move it to left of successor parent.
                if node to be removed is on right side of its parent node:
                    - move the successor node onto right of the parent node, thus replacing the node to be removed.
                    - if there is right subtree to the successor:
                        - move it to left of successor parent.
'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # def insertLeft(self, value):
    #     newNode = TreeNode(value)
    #     if self.left is None:
    #         self.left = newNode
    #     else:
    #         newNode.left = self.left
    #         self.left = newNode
    #     return newNode

    # def insertRight(self, value):
    #     newNode = TreeNode(value)
    #     if self.right is None:
    #         self.right = newNode
    #     else:
    #         newNode.right = self.right
    #         self.right = newNode
    #     return newNode

    def findMin(self):
        current = self
        parent = None

        if current.left is None and current.right is None:
            minNode = current
        while current.left:
            parent = current
            current = current.left
        minNode = current

        return minNode, parent

class BinarySearchTree:
    def __init__(self, root = None): # By default lets keep the root node as None. If we want to initialize it with a root node, then specify the value while creating an object.
        self.root = root

    def findMin(self,node):
        current = node
        parent = None

        if current.left is None and current.right is None:
            minNode = current
        while current.left:
            parent = current
            current = current.left
        # minNode = current

        return current, parent

    def insert(self, value):
        newNode = TreeNode(value)

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

                if value > current.value:
                    if current.right is None:
                        current.right = newNode
                        break
                    else:
                        current = current.right

        return newNode

    def searchNode(self,value):
        if self.root is None:
            return -1
        else:
            current = self.root
            parent = None
            while current:
                if current.value == value:
                    # print("Current: {} and Parent: {}".format(current.value, parent.value))
                    return current, parent
                elif value < current.value:
                    parent = current
                    current = current.left
                elif value > current.value:
                    parent = current
                    current = current.right
                else:
                    return None, None

    def removeNode(self, value):
        node, nodeParent = self.searchNode(value)
        successorNode, successorParent = self.findMin(node.right)
        if node is None:
            return False

        if node.left is None and node.right is None:
            if nodeParent is None:
                self.root.value = None
            elif node == nodeParent.left:
                nodeParent.left = None
            elif node == nodeParent.right:
                nodeParent.right = None

        elif node.left is None or node.right is None:
            if nodeParent is None:
                if node.left is not None:
                    node.value = node.left.value
                elif node.right is not None:
                    node.value = node.right.value
            elif node.left is not None:
                if node == nodeParent.left:
                    nodeParent.left = node.left
                elif node == nodeParent.right:
                    nodeParent.right = node.left
            elif node.right is not None:
                if node == nodeParent.left:
                    nodeParent.left = node.right
                elif node == nodeParent.right:
                    nodeParent.right = node.right

        elif node.left is not None and node.right is not None:
            # successorNode, successorParent = node.right.findMin()
            # print('Successor: {}'.format(successorNode.value))

            if nodeParent is None:
                node.value = successorNode.value
                if successorNode.right is not None:
                    successorParent.left = successorNode.right
            else:
                if node == nodeParent.left:
                    successorNode.left = node.left
                    nodeParent.left = successorNode
                    if successorNode.right is not None:
                        successorParent.left = successorNode.right

                elif node == nodeParent.right:
                    successorNode.left = node.left
                    nodeParent.right = successorNode
                    if successorNode.right is not None:
                        successorParent.left = successorNode.right

    def inOrderRecursive(self, root):
        if root is None:
            return

        self.inOrderRecursive(root.left)
        print(root.value, end=" ")
        self.inOrderRecursive(root.right)

    def inOrderIterative(self, root):
        current = root
        visitedNodes = []
        isTraversed = False

        if root is None:
            return

        while isTraversed is False:
            if current:
                visitedNodes.append(current)
                current = current.left
            else:
                if len(visitedNodes) > 0:
                    current = visitedNodes.pop()
                    print(current.value, end = " ")
                    current = current.right
                else:
                    isTraversed = True

    def preOrderRecursive(self, root):
        if root is None:
            return

        print(root.value, end = " ")
        self.preOrderRecursive(root.left)
        self.preOrderRecursive(root.right)

    def preOrderIterative(self, root):
        current = root
        visitedNodes = []
        isTraversed = False

        if root is None:
            return

        while isTraversed is False:
            if current:
                print(current.value, end = " ")
                visitedNodes.append(current)
                current = current.left
            else:
                if len(visitedNodes) > 0:
                    current = visitedNodes.pop()
                    current = current.right
                else:
                    isTraversed = True

    def postOrderRecursive(self, root):
        if root is None:
            return

        self.postOrderRecursive(root.left)
        self.postOrderRecursive(root.right)
        print(root.value, end = " ")

    def postOrderIterative(self,root):
        iteratorList = [root]
        tempList = []

        if root is None:
            return

        while len(iteratorList) > 0:
            current = iteratorList.pop()
            tempList.append(current.value)
            if current.left:
                iteratorList.append(current.left)
            if current.right:
                iteratorList.append(current.right)

        while len(tempList) > 0:
            print(tempList.pop(), end = " ")

    def breadthFirstTraversal(self, node):
        iteratorList = [node]

        if node is None:
            return

        while iteratorList:
            current = iteratorList.pop(0)
            print(current.value, end = " ")
            if current.left:
                iteratorList.append(current.left)
            if current.right:
                iteratorList.append(current.right)


if __name__ == '__main__':
    root = TreeNode(15)
    bst = BinarySearchTree(root)
    bst.insert(6)
    bst.insert(7)
    bst.insert(5)
    bst.insert(23)
    bst.insert(50)
    bst.insert(71)
    bst.insert(4)
    bst.insert(65)
    print("In-Order recursive method")
    bst.inOrderRecursive(root) # Output: Ascending order of nodes in BST - 4 5 6 7 15 23 50 71
    print('\n')
    print("In-Order iterative method")
    bst.inOrderIterative(root)
    print('\n')
    print(bst.searchNode(65)) # Output: "Node Found"
    print(bst.searchNode(10)) # Output: None
    bst.removeNode(6)
    print('\n')
    print("Pre-Order recursive method")
    bst.preOrderRecursive(root)
    print('\n')
    print("Pre-Order iterative method")
    bst.preOrderIterative(root)
    print('\n')
    print("Post-Order recursive method")
    bst.postOrderRecursive(root)
    print('\n')
    print("Post-Order iterative method")
    bst.postOrderIterative(root)
    print('\n')
    print("Breadth first traversal")
    bst.breadthFirstTraversal(root)
