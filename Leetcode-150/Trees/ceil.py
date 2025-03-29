def findCeil(root, x):
    # Write your code here.
    curr = root
    ceil = -1
    while curr:
        if curr.data >= x:
            ceil = curr.data
            curr = curr.left
        else:
            curr = curr.right
    return ceil


from os import *
from sys import *
from collections import *
from math import *


def floorInBST(root, X):

    # Write your Code here.
    curr = root
    floor_val = -1
    while curr:
        if curr.data <= X:
            floor_val = curr.data
            curr = curr.right
        else:
            curr = curr.left

    return floor_val
