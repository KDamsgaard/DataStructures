"""
Kristian Knudsen Damsgaard, 2019

The basic binary search tree components for the balanced binary search tree implementation.
"""

from node import Node
from datetime import datetime

class BinarySearchTree():
    def __init__(self):
        self.__root = None
        self.__errors = []


    

    def error_handler(self, node):
        error = str(datetime.now()) + ": " + str(node.get_data())
        self.__errors.append(error)
        print(error)

    def insert_node(self, key, data):

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
                if current_node.get_key() == key:
                    error = Node("error", "insert_node() error: Duplicate key.")
                    self.error_handler(error)
                    return error
                elif current_node.get_key() < key:
                    if current_node.get_right() is None:
                        current_node.set_right(new_node)
                        new_node.set_parent(current_node)
                        return new_node
                    else:
                        current_node = current_node.get_right()
                else:
                    if current_node.get_left() is None:
                        current_node.set_left(new_node)
                        new_node.set_parent(current_node)
                        return new_node
                    else:
                        current_node = current_node.get_right()

    #GETTERS    -----------------------------------------------------------------------------------------------

    def get_node(self, key):

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
        
    #PRINTERS   -----------------------------------------------------------------------------------------------

    def print_node(self, key):

        if self.get_node(key).get_key() == "error":
            error = Node("error", "print_node() error: Attempted to print non-Node object")
            self.error_handler(error)
            return error

        node = self.get_node(key)

        key = str(node.get_key())
        data = str(node.get_data())
        parent_key = "None"
        left_key = "None"
        right_key = "None"

        if node.get_parent() is not None:
            parent_key = str(node.get_parent().get_key())
        if node.get_left() is not None:
            left_key = str(node.get_left().get_key())
        if node.get_right() is not None:
            right_key = str(node.get_right().get_key())

        result = "_____________________________________\n"
        result += "" + key + ": " + data + "\n"
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

tree.print_node(0)
tree.print_node(1)
tree.print_node(2)
tree.print_node(3)



