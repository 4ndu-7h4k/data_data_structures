# LinkList insertions
from linklist import linkList as ll
from linklist import Node

# insert a element at head of the linklist
class linkList(ll):
    def __init__(self) -> None:
        super().__init__()
    # function to search a element in linklist
    def _insertElementAtFront(self,data):
        if(self.head != None):
            temp = self.head
            self.head = Node(data)
            self.head.nodeNext =temp
        else:
            self.head = Node(data)
    def _searching(self,data):
        if(self.head == None):
            return False
        else:
            temp = self.head
            while(temp != None):
                if(temp.nodeData == data):
                    return True
                else:
                    temp = temp.nodeNext
        return False
        
# initialize empty linklist
ll =linkList()
# adding the first element `1`
ll._insertElementAtFront(1)
# adding the second  element `2`
ll._insertElementAtFront(2)
print(ll._searching(1))
