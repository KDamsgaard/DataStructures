#
# Kristian Knudsen Damsgaard, 2019
#
# A binary search tree.
#
# The tree uses iterative rather than recursive methods.

from node import Node

class BinarySearchTree:

    def __init__(self):
        self.__root = None

    def insertNode(self, key, data) -> int:
        """
        Insert a node in the tree.
        Method sets root if tree is empty, otherwise iterates left or right from root depending 
        on key size, creating and setting a new node if empty child is found.

        @type key: integer
        @param key: The key of the node to insert.
        @type data: The data to attach to the new node        
        """

        try:
            key = int(key)
        except ValueError:
            print("insertNode() abort: Supplied key is not of type integer.")
            return -1
        
        if self.__root == None:
            self.__root = Node(key, data)
        else:
            done = False
            current_node = self.__root
            while not done:
                if current_node.getKey() == key:
                    print("insertNode() abort: Supplied key already exists.")
                    return -1
                elif current_node.getKey() < key:
                    if current_node.getRightChild() == None:
                        new_node = Node(key, data)
                        new_node.setParent(current_node)
                        current_node.setRightChild( new_node )
                        return 1
                    else:
                        current_node = current_node.getRightChild()
                else:
                    if current_node.getLeftChild() == None:
                        new_node = Node(key, data)
                        new_node.setParent(current_node)
                        current_node.setLeftChild( new_node )
                        return 1
                    else:
                        current_node = current_node.getLeftChild()
            
            #TODO: Rebalance
    
    def removeNode(self, key):
        """
        Method iterates left or right from root depending on key, setting right or left child of 
        node to be removed when found, then rearranges tree depending on node's children.

        @type key: integer
        @param key: The key of the node to remove.
        """
        
        try:
            key = int(key)
        except ValueError:
            print("removeNode() abort: Supplied key is not of type integer.")
            return -1

        old_node = self.getNode(key)
    
        if old_node.getLeftChild() is None and old_node.getRightChild() is None:
            print("removeNode() success: Node with key " + str(old_node.getKey()) + " removed." )
            old_node.__del__()

            #TODO: fix

        elif old_node.getLeftChild() is None and old_node.getRightChild() is not None:
            


            if old_node == self.__root:
                self.__root = old_node.getRightChild()
                
            
            
            old_node.__del__()
            print("removeNode() success: Node with key " + str(old_node.getKey()) + " removed." )

        elif old_node.getRightChild() is None and old_node.getLeftChild() is not None:
            old_node.getLeftChild().setParent(None)
            if old_node == self.__root:
                self.__root = old_node.getLeftChild()
            print("removeNode() success: Node with key " + str(old_node.getKey()) + " removed." )
            old_node.__del__()

        else:
            #TODO: rotate
            return -1

        #TODO: Rebalance

        

    #GETTERS    --------------------------------------------------------------------
    def getNode(self, key) -> Node:
        """ 
        Get a node from the tree.
        Method iterates left or right from root depending on key size, returning the node associated 
        with the key if found. Otherwise returns -1.

        @type key: integer
        @param key: The key of the node to get.

        @return_type: Node
        @return: The node belonging to the supplied key.
        """

        #TODO: Find out why returning an int works considering return type of method is set to Node

        if key != int(key):
            print("getNode() abort: Supplied key is not of type integer.")
            return -1
        
        if self.__root == None:
            print("getNode() abort: Tree is empty.")
            return -1
        else:
            current_node = self.__root
            done = False
            while not done:
                if current_node.getKey() == key:
                    print("getNode() returns: " + str(current_node.getKey()))
                    return current_node
                elif current_node.getKey() < key and current_node.getRightChild() is not None:
                    current_node = current_node.getRightChild()
                elif current_node.getKey() > key and current_node.getLeftChild() is not None:
                    current_node = current_node.getLeftChild()
                else:
                    print("getNode() abort: Key does not exist.")
                    return -1

    def getRoot(self) -> Node:
        return self.__root



