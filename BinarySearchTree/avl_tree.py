#
#Kristian Knudsen Damsgaard, 2019
#
#An AVL binary search tree.
#
#

from node import Node

class AVLTree:
    def __init__(self):
        self.__incrementingKey = 0
        self.__root = None
    
    #Add a node to the tree. Due to the nature of the autoincrementing key, 
    #nodes are always inserted to the right of the maximum key already in 
    #the tree
    def insertNode(self, data):
        #Create a new node
        new_node = Node(self.__incrementingKey, data)
        #If tree is empty, set the root of the tree to the new node
        if self.__incrementingKey == 0:
            self.__root = new_node
        self.__incrementingKey += 1

        #Set current node as node with highest key in tree
        current_node = self.findMaximumNode()

        #Append new node to current node as right child
        current_node.setRightChild(new_node)

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

    #GETTERS -------------------------------------------------------------
    def getIncrementingKey(self):
        return self.__incrementingKey
    
    def getRoot(self):
        return self.__root

#END OF CLASS "BST" ------------------------------------------------------


#TESTING

tree = AVLTree()

for i in range(0, 9):
    #print( "Loop key: " + str(tree.getIncrementingKey()) )
    data = "data_"+str(tree.getIncrementingKey())
    #print( "New data: " + data)
    tree.insertNode(data)





