class SimpleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    class Node:
        def __init__(self,ele):
            self.data = ele
            self.next = None

    def isEmpty(self):
        return self.count==0
    
    def getCount(self):
        return self.count
    
    def insertAtHead(self,ele):
        newnode = self.Node(ele)
        if not self.isEmpty():
            newnode.next = self.head
            self.head = newnode
        else:
            self.head = newnode
            self.tail = newnode
        self.count+=1

    def insertAtEnd(self,ele):
        newnode = self.Node(ele)
        if not self.isEmpty():
            self.tail.next = newnode
            self.tail = newnode
        else:
            self.tail = newnode
            self.head = newnode
        self.count+=1

    def getLL(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def isMember(self,ele):
        temp = self.head
        while temp != None:
            if ele == temp.data:
                return True
            temp = temp.next
        return False
    
    def removeFromTail(self):
        if not self.isEmpty():
            ele = self.tail.data
            temp = self.head
            while temp != None:
                if temp != self.tail:
                    print('current ',temp.data)
                    temp = temp.next 
                else:
                    break
            temp.next = None
            temp.data = None
            
            # temp.next = None
            self.count-=1
            return ele 