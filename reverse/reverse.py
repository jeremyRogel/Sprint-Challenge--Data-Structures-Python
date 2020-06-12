class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            #return true if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True

            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here then the target node isnt in our list
        return False

    def reverse_list(self, node, prev):
        if not self.head:
            return


        if not node.next_node:
            self.head = node
            node.next_node = prev
            return

        next = node.next_node

        node.next_node = prev

        self.reverse_list(next, node)