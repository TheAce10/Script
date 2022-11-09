
class Node:
    """
    A class to implement a node of a linked
    """

    # def __init__(self):
    #     self.head = None

    # def __repr__(self):
    #     node = self.head
    #     nodes = []
    #     while node is not None:
    #         nodes.append(node.data)
    #         node = node.next
    #     nodes.append("None")

    #     return " -> ".join(nodes)

    
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def __repr__(self):
        #returns string
        return self.data

class Linkedlist:
    """
    A class to implement a node of a linked
    """

    def __init__(self):
        self.head = None
        

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")

        return " -> ".join(nodes)

class Link:
    def __init__(self, contents=[]):
        self.head = None
        
        if contents is not None:
            node = Node(data = contents.pop(0))
            self.head = node

        for item in contents:
            node.next = Node(data = item)
            node = node.next