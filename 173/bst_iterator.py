# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, left, right):
        self.val = x
        self.left = left
        self.right = right

class Stack(object):
    def __init__(self):
        self.ls = []

    def push(self, x):
        self.ls.append(x)

    def pop(self):
        return self.ls.pop()

    def empty(self):
        return len(self.ls) == 0

    def peek(self):
        ret = self.ls.pop()
        self.ls.append(ret)
        return ret

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = Stack()

        if root == None:
            return

        curr = root
        self.stack.push(curr)
        self.root = root

        print "init: ", [n.val for n in self.stack.ls]

        # push to stack all the way to bottom left
        self.push_alltheway_left(curr)

    def hasNext(self):
        """
        :rtype: bool
        """
        return not self.stack.empty()
        

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return None

        ret = self.stack.pop()
        curr = ret
        if curr.right == None:
            pass
        else:
            curr = curr.right
            self.stack.push(curr)
            self.push_alltheway_left(curr)

        return ret.val

    def push_alltheway_left(self, curr):
        while curr.left != None:
            self.stack.push(curr.left)
            curr = curr.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())