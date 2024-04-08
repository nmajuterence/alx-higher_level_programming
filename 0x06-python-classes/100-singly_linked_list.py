class Node:
    """A class to represent a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize the Node instance.

        Args:
            data (int): The data value of the node.
            next_node (Node, optional): The reference
            to the next node. Defaults to None.

        Raises:
            TypeError: If data is not an integer or
            next_node is not a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the data of the node.

        Args:
            value (int): The data value to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the reference
        to the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the reference to the next node.

        Args:
            value (Node or None): The next node or None.

        Raises:
            TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value


class SinglyLinkedList:
    """A class to represent a singly linked list."""

    def __init__(self):
        """Initialize the SinglyLinkedList instance."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted
        position in the list (increasing order).

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """String representation of the singly linked list."""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()
