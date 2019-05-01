"""
Kristian Knudsen Damsgaard, 2019

The basic binary search tree components for the balanced binary search tree implementations (AVL and RedBlack).
"""

from node import Node
from datetime import datetime

class BinarySearchTree():
    def __init__(self):
        self.__root = None
        self.__errors = []

    def insert_node(self, key, data) -> Node:
        """
        Inserts a new node into the tree. Checks for non-integer and duplicate keys.

        @type key: integer
        @param key: The key of the node to insert
        @type data: any
        @param data: The data to include in the inserted node
        """
        try:
            key == int(key)
            new_node = Node(key, data)
        except ValueError:
            error = Node("error", "insert_node() error: Non-integer key.")
            self.error_handler(error)
            return error

        if self.__root == None:
            self.__root = new_node
        else:
            current_node = self.__root
            while True:
                if current_node.get_key() < key:
                    if current_node.get_right() is None:
                        current_node.set_right(new_node)
                        new_node.set_parent(current_node)
                        new_node.calc_and_set_height(new_node)
                        return new_node
                    else:
                        current_node = current_node.get_right()
                elif current_node.get_key() > key:
                    if current_node.get_left() is None:
                        current_node.set_left(new_node)
                        new_node.set_parent(current_node)
                        new_node.calc_and_set_height(new_node)
                        return new_node
                    else:
                        current_node = current_node.get_right()
                else: #current_node.get_key() == key
                    error = Node("error", "insert_node() error: Duplicate key.")
                    self.error_handler(error)
                    return error

    # Rotation diagram
    #     x     left -->    y
    #     /\    <-- right  /\
    #    A  y             x  C
    #       /\           /\
    #      B  C         A  B
    
    def left_rotate(self, key):

        x = self.get_node(key)
        y = x.get_right()

        attachment_point = x.get_parent()

        
 

        #
        x.set_right(y.get_left())
        x.set_parent(y)


        #right child becomes parent

        #right child's left child becomes right child



    
    def right_rotate(self, key):
        pass #TODO

    def error_handler(self, node):
        """
        Straps the data from an error node returned by another method to the errors list.
        The error node is a standard node set with "error" as key and error message as data.

        @type node: Node
        @param node: The error from which to get the error message
        """
        error = str(datetime.now()) + ": " + str(node.get_data())
        self.__errors.append(error)
        print(error)

    #GETTERS    -----------------------------------------------------------------------------------------------

    def get_node(self, key) -> Node:
        """
        Locates and returns the node belonging to supplied key. Checks for empty tree and non-existant key.

        @type key: integer
        @param key: The key of the node to return
        """
        if self.__root == None:
            error = Node("Error", "get_node() error: Empty tree.")
            self.error_handler(error)
            return error
        
        current_node = self.__root

        while True:
            if current_node.get_key() == key:
                return current_node
            elif current_node.get_key() > key and current_node.get_left() is not None:
                current_node = current_node.get_left()
            elif current_node.get_key() < key and current_node.get_right() is not None:
                current_node = current_node.get_right()
            else:
                error = Node("error", "Tried to get non-existant node.")
                self.error_handler(error)
                return error
    
    def get_errors(self):
        return self.__errors
    #PRINTERS   -----------------------------------------------------------------------------------------------

    def print_node(self, node) -> Node:
        """
        Prints information about a node.

        @type node: Node
        @param node: The node to print
        """

        #TODO: Move to Node class

        key = str(node.get_key())
        data = str(node.get_data())
        parent_key = "None"
        left_key = "None"
        right_key = "None"
        height = str(node.get_height())

        if node.get_parent() is not None:
            parent_key = str(node.get_parent().get_key())
        if node.get_left() is not None:
            left_key = str(node.get_left().get_key())
        if node.get_right() is not None:
            right_key = str(node.get_right().get_key())
        

        result = "_____________________________________\n"
        result += "" + key + ": " + data + ", height: " + str(height) + "\n"
        if node == self.__root:
            result += "ROOT "
        else:
            result += "Parent: " + parent_key + " "
        result += "Left: " + left_key + " Right: " + right_key
        print(result)

#END OF CLASS "Node"    ---------------------------------------------------------------------------------------

#TESTING    ---------------------------------------------------------------------------------------------------

tree = BinarySearchTree()

# tree.get_node(0)
# tree.insert_node("wrong_key", "data_wrong_key")

tree.insert_node(1, "1_data")
tree.insert_node(0, "0_data")
tree.insert_node(2, "2_data")
tree.insert_node(3, "3_data")
tree.insert_node(4, "4_data")

tree.print_node(tree.get_node(0))
tree.print_node(tree.get_node(1))
tree.print_node(tree.get_node(2))
tree.print_node(tree.get_node(3))
tree.print_node(tree.get_node(4))

# print(tree.get_errors())



