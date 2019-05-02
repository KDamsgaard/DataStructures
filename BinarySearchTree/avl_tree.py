"""
Kristian K. Damsgaard, 2019

An AVL implementation for the binary search tree.
"""

from binary_search_tree import BinarySearchTree as BST
from node import Node

class AVL(BST):
    """
    Note inheritance from BinarySearchTree.
    """
    def __init__(self):
        BST.__init__(self)

    def insert_balanced(self, key, data):
        new_node = self.insert_node(key, data)

        return new_node
        

#END OF CLASS "AVL"     -------------------------------------------------------------------------------

#TESTING        ---------------------------------------------------------------------------------------


avl = AVL()

avl.insert_balanced(0, "0_data")

print(avl.find_node(0).get_key())
        