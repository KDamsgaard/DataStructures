#
# Kristian Knudsen Damsgaard, 2019
#
# A node for use in binary search tree (bst.py)
#

class Node:
    def __init__(self, key, data):
        self.__key = key
        self.__data = data
        self.__parent = None
        self.__left = None
        self.__right = None

    def __del__(self):
        self.__key = None
        self.__data = None
        self.__parent = None
        self.__left = None
        self.__right = None
    

    #SETTERS -------------------------------------------------------------
    def set_parent(self, node):
        self.__parent = node
    
    def set_right(self, node):
        self.__right = node

    def set_left(self, node):
        self.__left = node

    #GETTERS -------------------------------------------------------------

    def get_key(self):
        return self.__key

    def get_data(self):
        return self.__data

    def get_parent(self):
        return self.__parent

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right
        
#END OF CLASS "Node" -----------------------------------------------------