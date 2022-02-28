from linklist import linkList as ll,Node
class linkList(ll):
    def __init__(self) -> None:
        super().__init__()
    def _insertElementAtFront(self,data) -> None:
        if(self.head != None):
            temp = self.head
            self.head = Node(data)
            self.head.nodeNext =temp
        else:
            self.head = Node(data)
   # function to search a element in linklist
    def _searching(self,data) -> bool:
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
    #function to delete a element from linklist
    def _deletion(self,data) -> None:
        if(self.head == None):
            return
        else:
            temp = self.head
            if temp.nodeData == data:  
                self.head = self.head.nodeNext
                return
            while(temp.nodeNext!=None):
                if(temp.nodeNext.nodeData == data):
                    temp.nodeNext = temp.nodeNext.nodeNext
                else:
                    temp = temp.nodeNext
            
                    
        
# initialize empty linklist
ll =linkList()
# adding the first element `1`
ll._insertElementAtFront(1)
# adding the second  element `2`
ll._insertElementAtFront(2)
ll._insertElementAtFront(3)

print(ll._searching(1))
print(ll._searching(2))
ll._deletion(3)
print(ll._searching(3))

