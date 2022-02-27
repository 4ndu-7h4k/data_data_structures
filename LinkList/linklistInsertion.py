# LinkList insertions
from linklist import linkList as ll
from linklist import Node

# insert a element at head of the linklist
class linkList(ll):
    def __init__(self) -> None:
        super().__init__()
    def _insertElementAtFront(self,data):
        if(self.head != None):
            temp = self.head
            self.head = Node(data)
            self.head.nodeNext =temp
        else:
            self.head = Node(data)
# initialize empty linklist
ll =linkList()
# adding the first element `1`
ll._insertElementAtFront(1)
# adding the second  element `2`
ll._insertElementAtFront(2)
#to print the first element
print(ll.head.nodeData)
#to print the second element
print(ll.head.nodeNext.nodeData)
