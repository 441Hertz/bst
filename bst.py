class BST():
    def __init__(self, val = None):
        self.val = val
        self.right = None
        self.left = None
        self.count = 1
    def add(self, val):
        if not self.val:
            self.val = val
        elif val > self.val:
            if self.right != None:
                self.right.add(val)
            else:
                self.right = BST(val)
        elif val < self.val:
            if self.left != None:
                self.left.add(val)
            else:
                self.left = BST(val)
        elif self.val == val:
            self.count += 1
    def get_min(self):
        if self.left is not None:
            return self.left.get_min()
        else:
            return self.val
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
    def has_right(self):
        return self.right != None
    def has_left(self):
        return self.left is not None
    def delete(self, val):
        if val > self.val and self.has_right():
            if self.right.val == val:
                if self.right.count > 1:
                    self.right.count -= 1
                else:
                    self.right = None
            else:
                self.right.delete(val)
        elif val < self.val and self.has_left():
            if self.left.val == val:
                if self.left.count > 1:
                    self.left.count -= 1
                else:
                    self.left = None
            else:
                self.left.delete(val)
        else:
            print(f'{val} does not exist')
    def has_single_child(self):
        return [self.has_left(), self.has_right()].count(True) == 1
    def all_nodes(self):
        nodes = [self]
        if self.has_left():
            nodes += self.left.all_nodes()
        if self.has_right():
            nodes += self.right.all_nodes()
        return nodes
    def sum_single_child_nodes(self):
        counter = 0
        for node in self.all_nodes():
            if node.has_single_child():
                counter += node.count
        return counter
    def clear(self):
        self.val = None
        self.right = None
        self.left = None
        self.counter = 1

s1='abracadabracabob'
s2='American Computer Science League'
s3='Python and Java are programming languages'
s4='Python and Java and java and python'
s5='the quick brown fox jumped over the lazy river'

root = BST()
import string
def convert(letter):
    return string.ascii_lowercase.index(letter)
root = BST()
for value in [s1, s2, s3, s4, s5]:
    value = value.lower()
    value = value.replace(' ', '')
    for letter in value:
        num = convert(letter)
        root.add(num)
    print(root.sum_single_child_nodes())
    root.clear()