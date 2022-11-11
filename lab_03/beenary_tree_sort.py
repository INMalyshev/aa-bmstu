import random

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if self.val > val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)
    
    def get_sorted(self, dst):
        if self.left is not None:
            self.left.get_sorted(dst)
        dst.append(self.val)
        if self.right is not None:
            self.right.get_sorted(dst)
    
    def sort(self):
        dst = []
        self.get_sorted(dst)
        return dst


def beenary_tree_sort(arr):
    if len(arr) == 0:
        return arr
    
    head = Node(arr[0])
    for i in range(1, len(arr)):
        head.insert(arr[i])
    
    return head.sort()
