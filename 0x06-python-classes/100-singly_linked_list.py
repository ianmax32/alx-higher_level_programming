#!/usr/bin/python3

"""
this is a module that has classes Node and
SingilyLinkedList class
"""


class Node:
    """
    this is the class node that defines
    a singlily linkedlist
    """
    def __init__(self, data, next_node=None):
        """
        this is the init method that defines the
        class instance
        Args:
            data (int): data in the node of a list
            next_node (Node): points to the next
            node ot the list
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """this method returns the data in a node"""
        return self.__data

    @data.setter
    def data(self, value):
        """this method sets the value to the data field"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """this method returns the next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """this method sets the value of next_node or None"""
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

    def __str__(self):
        return str(self.__data)


"""this class defines a singily linked list using a Node class"""


class SinglyLinkedList:
    """this class represents a singlylinkedlist"""
    def __init__(self):
        """init method to define the instance head of the class"""
        self.__head = None

    def sorted_insert(self, value):
        """this method inserts a new Node into
        the correct sorted position in the list
        increasing order"""
        list_head = self.__head

        if not list_head:
            self.__head = Node(value)
            return
        if list_head.data > value:
            self.__head = Node(value, list_head)
            return
        while list_head.next_node:
            if list_head.next_node.data >= value:
                list_head.next_node = Node(value, list_head.next_node)
                return
            list_head = list_head.next_node
        list_head.next_node = Node(value)

    def __str__(self):
        """this method prints the class fields"""
        all_nodes = []
        list_head = self.__head
        while list_head:
            all_nodes.append(str(list_head))
            list_head = list_head.next_node
        return "\n".join(all_nodes)
