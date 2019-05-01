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
        self.__height = 0

    def __del__(self):
        self.__key = None
        self.__data = None
        self.__parent = None
        self.__left = None
        self.__right = None
        self.__height = None

    def calc_and_set_height(self, node):
        height = self.calculate_height(node)
        self.set_height(height)
    
    def calculate_height(self, node):
        if node is None:
            return 0
        else:
            print ("calcing")
            return max(self.calculate_height(self.__left), self.calculate_height(self.__right)) + 1



    #SETTERS -------------------------------------------------------------
    def set_parent(self, node):
        self.__parent = node

    def set_left(self, node):
        self.__left = node
    
    def set_right(self, node):
        self.__right = node

    def set_height(self, height):
        self.__height = height
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
    
    def get_height(self):
        return self.__height
        
#END OF CLASS "Node" -----------------------------------------------------