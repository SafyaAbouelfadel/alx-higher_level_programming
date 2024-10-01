#!/usr/bin/python3
"""Defines classes for a singly-linked list"""


class Node:
    """Represantation of a node in a singly-linked list"""

    def __init__(self, data, next_node=None):
        """Constructor of a new Node
        Args:
            data (int): data of the new Node.
            next_node (Node): next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data of the Node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get or set the next_node of the Node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly-linked list"""

    def __init__(self):
        """Initalizes a new SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node to the SinglyLinkedList
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Define the print func representation of a SinglyLinkedList."""
        vals = []
        temp = self.__head
        while temp is not None:
            vals.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(vals))
