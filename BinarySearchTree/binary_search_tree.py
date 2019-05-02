"""
Kristian K. Damsgaard, 2019

The basic binary search tree components for the balanced binary search tree implementations (AVL and RedBlack).
"""

# import sys
# sys.path.append("c:\code\pythonlibs")

from node import Node
from datetime import datetime
from stopwatch import Stopwatch

class BinarySearchTree():
    def __init__(self):
        self.__root = None
        self.__errors = []

    def insert_node(self, key, data) -> Node:
        """
        Inserts a new node into the tree. Checks for non-integer, negative and duplicate keys.

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

        if key < 0:
            error = Node("error", "insert_node() error: Negative key.")

        if self.__root == None:
            new_node.set_height(0)
            self.__root = new_node
        else:
            current_node = self.__root
            while True:
                if current_node.get_key() < key:
                    if current_node.get_right() is None:
                        current_node.set_right(new_node)
                        new_node.set_parent(current_node)
                        new_node.set_height(self.calc_node_depth(new_node))
                        return new_node
                    else:
                        current_node = current_node.get_right()
                elif current_node.get_key() > key:
                    if current_node.get_left() is None:
                        current_node.set_left(new_node)
                        new_node.set_parent(current_node)
                        new_node.set_height(self.calc_node_depth(new_node))
                        return new_node
                    else:
                        current_node = current_node.get_right()
                else: #current_node.get_key() == key
                    error = Node("error", "insert_node() error: Duplicate key.")
                    self.error_handler(error)
                    return error

    def remove_node(self, node):
        #find the node
        #if node has 0 children
            #remove
        #if node has 1 child
            #set parent as parent of child
            #delete node
        #if node has 2 children
            #find highest depth
            #set parent as parent of tallest subtree
            #remove node
        pass

    def calc_node_depth(self, node):
        """
        Iteratively calculates the distance from a node to the root.

        @type node: Node
        @param node: The node to measure the depth of.
        """
        current_node = node
        height = 0
        while current_node.get_parent() is not None:
            current_node = current_node.get_parent()
            height += 1
        return height

    def calc_node_height(self, node):
        """
        Recursively calculates height os a node.

        @type node: Node
        @param node: The node to calculate the height of.
        """
        if node is None:
            return -1 #Subtracting 1 at end of recursion ensures correct computation of height
        else:
            left_height = self.calc_node_height(node.get_left())
            right_height = self.calc_node_height(node.get_right())

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    # Rotation diagram
    #     x     left -->    y
    #     /\    <-- right  /\
    #    A  y             x  C
    #       /\           /\
    #      B  C         A  B
    
    def left_rotate(self, key):

        # x = self.find_node(key)
        # y = x.get_right()

        #TODO: Research iterative rotate (and wether it is worth it)
        pass

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

    def find_node(self, key) -> Node:
        """
        Locates and returns the node belonging to supplied key. Checks for empty tree and non-existent key.

        @type key: integer
        @param key: The key of the node to return
        """
        if self.__root == None:
            error = Node("Error", "find_node() error: Empty tree.")
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
            else: #Iteration reaches null node without finding key
                error = Node("error", "Tried to get non-existent node.")
                self.error_handler(error)
                return error
    
    def get_errors(self):
        return self.__errors

    #PRINTERS   -----------------------------------------------------------------------------------------------

    def print_tree(self, node):
        #TODO: Implement
        pass

#END OF CLASS "Node"    ---------------------------------------------------------------------------------------

#TESTING    ---------------------------------------------------------------------------------------------------

timer = Stopwatch()
timer.start()

tree = BinarySearchTree()

# tree.find_node(0)
# tree.insert_node("wrong_key", "data_wrong_key")

tree.insert_node(1, "1_data")
tree.insert_node(0, "0_data")
tree.insert_node(2, "2_data")
tree.insert_node(3, "3_data")
tree.insert_node(4, "4_data")

tree.find_node(0).print_node()
tree.find_node(1).print_node()
tree.find_node(2).print_node()
tree.find_node(3).print_node()
tree.find_node(4).print_node()
print("_____________________________________\n")

print ("Height of 0: " + str(tree.calc_node_height(tree.find_node(0))))
print ("Height of 1: " + str(tree.calc_node_height(tree.find_node(1))))
print ("Height of 2: " + str(tree.calc_node_height(tree.find_node(2))))
print ("Height of 3: " + str(tree.calc_node_height(tree.find_node(3))))
print ("Height of 4: " + str(tree.calc_node_height(tree.find_node(4))))

# print(tree.get_errors())

# work = 0
# for i in range(0, 100000):
#     work += 1

timer.stop()

print("Time elapsed: " + str(timer.get_time_elapsed()))



