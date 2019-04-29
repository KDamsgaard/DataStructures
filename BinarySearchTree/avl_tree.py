#
#Kristian Knudsen Damsgaard, 2019
#
#An AVL implementation for the binary search tree.
#
#

from binary_search_tree import BinarySearchTree as BST
from node import Node

class AVLTree(BST):
    def __init__(self):
        #Since no database exists the incrementing key is set to 0.
        self.__incrementingKey = 0
        self.__root = None
    
    #Add a node to the tree. Due to the nature of the autoincrementing key, 
    #nodes are always inserted to the right of the maximum key already in 
    #the tree.
    def insertNode(self, data):
        #Create a new node
        new_node = Node(self.__incrementingKey, data)
        #If tree is empty, set the root of the tree to the new node 
        #and increment key.
        if self.__incrementingKey == 0:
            self.__root = new_node
            self.__incrementingKey += 1
        #Else iterate right until right child is None, then set current_node
        #as parent of new node, set right child of current node to new node 
        #and increment key.
        else:
            current_node = self.__root
            while current_node.getRightChild() is not None:
                current_node = current_node.getRightChild()
            new_node.setParent(current_node)
            current_node.setRightChild(new_node)
            self.__incrementingKey += 1
        #Measure tree balance
        #TODO: Make balance measure method
        #Balance if needed
        #TODO: Make balance method

    #Removes a specific node from the tree
    def removeNode(self, node):
        #TODO: implement
        return -1

    #Locates a specific node from the tree
    def findNode(self, key, node):
        #TODO: implement
        return -1

    def leftRotation(self):
        return -1
    
    def rightRotation(self):
        return -1

    #GETTERS -------------------------------------------------------------
    def getIncrementingKey(self):
        return self.__incrementingKey
    
    def getRoot(self):
        return self.__root

#END OF CLASS "BST" ------------------------------------------------------


#TESTING

tree = AVLTree()

for i in range(0, 10):
    print( "Loop key: " + str(tree.getIncrementingKey()) )
    data = "data_"+str(tree.getIncrementingKey())
    print( "New data: " + data)
    tree.insertNode(data)
    print( "New key: " + str(tree.getIncrementingKey()) )





