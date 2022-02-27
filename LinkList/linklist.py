"""
A linked list is a linear data structure, 
in which the elements are not stored at contiguous memory locations.
"""
# Node object 
class Node:
    # initialize node object
    def __init__(self,dataVal=None) -> None:
        self.nodeData = dataVal
        self.nodeNext = None
# Linklist holds the node object
class linkList:
    """
    linkList 
    """
    def __init__(self) -> None:
        self.head=None

