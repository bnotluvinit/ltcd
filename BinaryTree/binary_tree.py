class TreeNode(object):
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if self.value:
            if value < self.value:
                    if self.left is None:
                        self.left = TreeNode(value)
                    else:
                        self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = value
                else:
                    self.right.insert(value)
            else:
                self.value = value

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.val),
        if self.right:
            self.right.PrintTree()