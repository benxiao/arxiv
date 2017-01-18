class Node:
    def __init__(self, v, left=None, right=None, parent=None):
        self.v = v
        self.left=left
        self.right=right
        self.parent=parent




def squeeze(root):
    if root:
        if not (root.left and root.right):
            if root.left:
                left = root.left
                root.v.extend(left.v)
                root.left = left.left
                root.right = left.right
                squeeze(left.left)
                squeeze(left.right)

            elif root.right:
                right = root.right
                root.v.extend(right.v)
                root.right = right.right
                root.left = right.left
                squeeze(right.right)
                squeeze(right.left)

        if root.left and root.right:
            squeeze(root.left)
            squeeze(root.right)




if __name__ == '__main__':
    tree = Node([1])
    tree.left = Node([2])
    tree.left.parent = tree
    tree.right = Node([3])
    tree.right.parent = tree
    right = tree.right
    right.left = Node([4])
    right.left.parent = right
    squeeze(tree)
    print(tree.v)
    print(tree.left.v)
    print(tree.right.v)




