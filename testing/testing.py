class Tree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self,data):
            self.data = data
            self.left = None
            self.right = None

    def insert(self,ele):
        self.root = self._insert_(self.root,ele)

    def _insert_(self,node,ele):
        if node ==None:
            return self.Node(ele)
        elif node.data>ele :
            node.left = self._insert_(node.left,ele)
        elif node.data<ele :
            node.right = self._insert_(node.right,ele)
        return node
    def inorder(self):
        self._inorder_(self.root)
    
    def _inorder_(self,node):
        if node:
            self._inorder_(node.left)
            print(node.data)
            self._inorder_(node.right)

    def delete(self):
        pass

    def isinstence(self,key):
        return self._isinstence_(self.root,key)
    
    def _isinstence_(self,node,key):
        if node!=None:
            if node.data==key:
                return True
            elif key<node.data:
                return self._isinstence_(node.left,key)
            elif node.data<key:
                return self._isinstence_(node.right,key)
        return False
        
class Queue:
    def __init__(self,size):
        self.data = [None]*size
        self.front = 0
        self.rear = 0
        self.count= 0
    
    def isEmpty(self):
        return self.count==0
    
    def isFull(self):
        return self.rear==len(self.data)
    
    def enqueue(self,ele):
        if not self.isFull():
            self.data[self.rear] = ele
            self.rear +=1
            self.count+=1
            print(self.data)
            
    def dequeue(self):
        if not self.isEmpty():
            self.data[self.front] = None
            self.count -=1
            self.front +=1
            print(self.data)

class flexQueue:
    def __init__(self,size):
        self.data = [None]*size
        self.front = 0
        self.rear = 0
        self.count= 0
    
    def enqueue(self,ele):
        if self.count==len(self.data):
            self.resize(len(self.data)*2)    
        self.data[self.rear] = ele
        self.rear = (self.rear+1)%len(self.data)
        self.count+=1
        print(self.data)
            
    def dequeue(self):
        if self.count<len(self.data)//2:
            self.resize(len(self.data)//2)
        self.data[self.front] = None
        self.front = (self.front+1)%len(self.data)
        self.count-=1
        print(self.data)

    def resize(self,size):
        newdata = [None]*size
        for i in range(self.count):
            newdata[i] = self.data[(self.front+i)%len(self.data)]
        self.front = 0
        self.rear = self.count
        self.data = newdata

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.count = 0
        pass

    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
        
    def isEmpty(self):
        return self.count==0
    
    def getall(self):
        temp = self.head
        while temp!=None:
            print(temp.data)
            temp = temp.next

    def inserthead(self,ele):
        newnode = self.Node(ele)
        if not self.isEmpty():
            newnode.next = self.head
            self.head = newnode
        else:
            self.tail = self.head = newnode
        self.count+=1

    def insertail(self,ele):
        newnode = self.Node(ele)
        if not self.isEmpty():
            self.tail.next = newnode
            self.tail = newnode 
        else:
            self.tail = self.head = newnode
        self.count+=1

    def deleteatHead(self):
        if not self.isEmpty():
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.count-=1
    
    def deleteTail(self):
        temp =self.head
        while temp.next != self.tail:
            temp = temp.next
        temp.next = None
        self.tail = temp
        self.count-=1

    def insertafterelement(self,key,ele):
        if not self.isEmpty():

            if self.tail.data == key:
                self.insertail(key)

            temp = self.head
            while temp.data != key:
                temp = temp.next
            newNode = self.Node(ele)
            nextaddress = temp.next
            temp.next = newNode
            newNode.next = nextaddress

    def deletbeorelement(self,key):
        if not self.isEmpty():
            temp = self.head
            while temp.next.next.data !=key:
                temp = temp.next
            var = temp.next
            temp.next = temp.next.next
            var.next = None
            self.count-=1
        