"""
Kristian K. Damsgaard, 2019

A node for use in binary search tree
"""

class Node:
    def __init__(self, key, data):
        self.__key = key
        self.__data = data
        self.__parent = None
        self.__left = None
        self.__right = None
        self.__depth = -1

    def __del__(self):
        self.__key = None
        self.__data = None
        self.__parent = None
        self.__left = None
        self.__right = None
        self.__depth = None

    #PRINTERS   ------------------------------------------------------------------------------------
    def print_node(self) -> str:
        """
        Prints information about a node.

        @type node: Node
        @param node: The node to print
        """

        parent = "Parent: "
        left = "Left: "
        right = "Right: "

        if self.__parent is not None:
            parent += str(self.__parent.get_key()) + ", "
        else:
            parent += "ROOT, "
        
        if self.__left is not None:
            left += str(self.__left.get_key()) + ", "
        else:
            left += "None, "

        if self.__right is not None:
            right += str(self.__right.get_key()) + ", "
        else:
            right += "None, "

        result = "_____________________________________\n" \
            + "Key: " + str(self.__key) + ", depth: " + str(self.__depth) + "\n" \
            + left + parent + right

        print(result)

    #SETTERS    ------------------------------------------------------------------------------------
    def set_parent(self, node):
        self.__parent = node

    def set_left(self, node):
        self.__left = node
    
    def set_right(self, node):
        self.__right = node

    def set_height(self, height):
        self.__depth = height
    #GETTERS    -------------------------------------------------------------------------------------

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
        return self.__depth
        
#END OF CLASS "Node" -----------------------------------------------------