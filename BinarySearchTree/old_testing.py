#
#Kristian Knudsen Damsgaard, 2019
#
#Testing for the binary tree project
#
#

from binary_search_tree import BinarySearchTree as BST
from avl import AVL



#TESTING BinarySearchTree -------------------------------------------------------------------------

tree = BST()           
# #Tests getNode() on empty tree
# print(tree.getNode(0))         
# #Tests getNode() with non-integer argument
# tree.insertNode("ti", "data_ti")
# #Tests insertNode() on empty tree
# tree.insertNode(10, "data_10")
# #Tests getNode()
# print( "Key 10: " + str(tree.getNode(10).getKey()) )
# #Tests insertNode() on duplicate key
# tree.insertNode(10, "data_10")
# #Tests insertNode() on non-empty tree (left side)
# tree.insertNode(9, "data_9")
# print( "Key 9: " + str(tree.getNode(9).getKey()) )
# #Tests insertNode() on non-empty tree (right side)
# tree.insertNode(11, "data_11")
# print( "Key 11: " + str(tree.getNode(11).getKey()) )
# # Tests getParent()
# print( "Parent of 9: " + str(tree.getNode(9).getParent().getKey()) )
# #Tests getRightChild()
# print( "Node 10, right: " + str(tree.getNode(10).getRightChild().getKey()) )
# #Tests getLeftChild()
# print( "Node 10, left: " + str(tree.getNode(10).getLeftChild().getKey()) )
# #Tests getNode() with non-existant key
# tree.getNode(1)
# tree.insertNode(1, "data_1")
# print( "Key 1: " + str(tree.getNode(1).getKey()) )

tree.insertNode(0, "data_0")
tree.insertNode(1, "data_1")
# tree.insertNode(0, "data_0")
tree.insertNode(2, "data_2")

# tree.removeNode(0)
# print(tree.getRoot().getKey())

print( "Right child of 0: " + str(tree.getNode(0).getRightChild().getKey()) )
print( "Parent of 2: " + str(tree.getNode(2).getParent().getKey()) )
print(tree.getNode(1).getKey())

tree.removeNode(1)
print( "Right child of 0: " + str(tree.getNode(0).getRightChild().getKey()) )
print( "Parent of 2: " + str(tree.getNode(2).getParent().getKey()) )
# print(tree.getNode(1))

# tree.insertNode(-1, "data_-1")
# tree.insertNode(-2, "data_-2")

# print( "Left child of 0: " + str(tree.getNode(0).getLeftChild().getKey()) )
# print( "Parent of -2: " + str(tree.getNode(-2).getParent().getKey()) )
# print(tree.getNode(-1).getKey())

# tree.removeNode(-1)
# print( "Left child of 0: " + str(tree.getNode(0).getLeftChild().getKey()) )
# print( "Parent of -2: " + str(tree.getNode(-2).getParent().getKey()) )
# print(tree.getNode(-1))
