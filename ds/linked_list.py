"""
Author: Prabakaran Santhanam 
email: praba230890@gmail.com
"""

class Node():
    """
        Nodes of a linked list can be created using this Node class
    """
    def __init__(self, val, nxt=None) -> None:
        self.val = val
        self.next = nxt
    
    def __repr__(self) -> str:
        return str(self.val)

class LinkedList():
    """
        Linked list is a set of nodes that are sequentially lined through each other using pointers
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, val):
        """
            Append an element to the end of a linked list.

            If no element is present, then a new node will be created and it will be 
            set as both the head and tail of the LL
        """
        if not self.head:
            self.head = self.tail = Node(val)
        else:
            tail = self.tail
            self.tail = Node(val, tail)
        self.length += 1

    def add(self, val):
        """
            Append an element to the end of a linked list.

            If no element is present, then a new node will be created and it will be 
            set as both the head and tail of the LL
        """
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
        else:
            tail = self.tail
            self.tail = Node(val, tail)
        self.length += 1
    
    def __str__(self) -> str:
        ll = ""
        cur = self.head
        print(self.head.next, self.head.next.next)
        while cur:
            print(cur)
            cur = cur.next
        return ll

    def __repr__(self) -> str:
        return f"Head: {self.head.val}, Tail: {self.tail.val}, Length: {self.length}"
