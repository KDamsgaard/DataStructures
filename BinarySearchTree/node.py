#
# Kristian Knudsen Damsgaard, 2019
#
# A node for use in binary search tree (bst.py)
#

class Node:
    def __init__(self, key, data):
        self.__key = key
        self.__data = data
        self.__left = None
        self.__right = None
    

    #SETTERS -------------------------------------------------------------
    def setRightChild(self, node):
        self.__right = node

    def setLeftChild(self, node):
        self.__left = node

    #GETTERS -------------------------------------------------------------

    def getKey(self):
        return self.__key

    def getData(self):
        return self.__data

    def getLeftChild(self):
        return self.__left

    def getRightChild(self):
        return self.__right
        
#END OF CLASS "Node" -----------------------------------------------------