#
#Kristian Knudsen Damsgaard, 2019
#
#An AVL binary search tree.
#
#

import array as arr
from node import Node

class AVLTree:
    #Initializer
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
        
        #Increment key 
        self.__incrementingKey += 1

        #Set current node as node with highest key in tree
        current_node = self.findMaximumNode()

        #Append new node to current node as right child
        current_node.setRightChild(new_node)

        #Measure tree balance
        #TODO: Make balance measure method

        #Balance if needed
        #TODO: Make balance method

    #Finds the node associated with the key of highest value in the tree.
    #The highest key will always be located on the farthest right side of 
    #the tree
    #@return: the node with the highest key in the tree
    def findMaximumNode(self):
        if self.__root is None:
            return None
        else:
            current_node = self.__root
            print( current_node.getKey() ) #TESTING

        print("max.right.data: " + str(current_node.getRightChild().getData()))
        
        # while current_node.getRightChild() is not None:
        #     next_node = current_node.getRightChild()
        #     current_node = next_node


        #     # current_node = current_node.getRightChild()

        #     print(current_node.getData())#TESTING
        
        return current_node

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

# print( "key: " + str(tree.getRoot().getKey()) )
# print( "data: " + str(tree.getRoot().getData()) )
# print( "key: " + str(tree.findMaximumNode().getKey()) )
# print( "data: " + str(tree.findMaximumNode().getData()) )




