'''
QUESTION -
----------
https://leetcode.com/problems/subtree-of-another-tree/

APPROACH -
----------
    1. For given 2 trees, find pre-order and in-order for both.
    2. If subtree_preorder is subset(with same order) of maintree_preorder: return true
    3. If subtree_inorder is subset(with same order) of maintree_inorder: return true
    4. Both conditions 2 and 3 should be true.



'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root = None): # By default lets keep the root node as None. If we want to initialize it with a root node, then specify the value while creating an object.
        self.root = root

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

    def preOrder(self,root,lst):
        if root is None:
            return

        lst.append(root.value)
        self.preOrder(root.left, lst)
        self.preOrder(root.right, lst)

        return lst

    def inOrder(self,root,lst):
        if root is None:
            return

        self.inOrder(root.left, lst)
        lst.append(root.value)
        self.inOrder(root.right, lst)

        return lst

    def isSubTree(self, root1, root2):
        treeListPreOrder = self.preOrder(root1,[])
        subTreeListPreOrder = self.preOrder(root2,[])
        treeListInOrder = self.inOrder(root1,[])
        subTreeListInOrder = self.inOrder(root2,[])

        if self.isSubList(treeListInOrder, subTreeListInOrder) and self.isSubList(treeListPreOrder, subTreeListPreOrder):
            return True
        else:
            return False

    def isSubList(self,mainLst, subLst):

        if subLst == []:
            return True
        elif mainLst == subLst:
            return True
        elif len(subLst) > len(mainLst):
            return False
        else:
            mainStr = " ".join(str(element) for element in mainLst)
            subStr = " ".join(str(element) for element in subLst)
            if subStr in mainStr:
                return True

if __name__ == '__main__':
    root1 = TreeNode(6)
    root2 = TreeNode(12)
    bst1 = BinarySearchTree(root1)
    bst2 = BinarySearchTree(root2)
    bst1.insert(4)
    bst1.insert(2)
    bst1.insert(5)
    bst1.insert(9)
    bst1.insert(12)
    bst1.insert(8)
    bst1.insert(10)
    bst1.insert(14)
    bst2.insert(10)
    bst2.insert(14)
    print(bst2.isSubTree(root1, root2))
    print(bst1.inOrder(root1,[]))
