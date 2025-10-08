class sortingLogic:
    def __init__(self,data):
        self.data = data

    def swap(self,i,j):
        self.data[i],self.data[j] = self.data[j],self.data[i]

    def Buble(self):
        print(self.data)
        for i in range(len(self.data)):
            for j in range(len(self.data)-i-1):
                if self.data[j]>self.data[j+1]:
                    self.swap(j,j+1)
        print(self.data)
    
    def selection(self):
        print(self.data)
        for i in range(len(self.data)):
            temp=i
            for j in range(i,len(self.data)-i):
                if self.data[temp]>self.data[j]:
                    temp=j
            self.swap(temp,i)
        print(self.data)

    def insertion(self):
        print(self.data)
        for i in range(1,len(self.data)):
            temp = self.data[i]
            j=i-1
            while j>=0 and temp<self.data[j]:
                self.data[j+1] = self.data[j]
                j-=1
            self.data[j+1] = temp
        print(self.data)
    
    def quick(self):
        print(self.data)
        self._quick(0,len(self.data)-1)
        print(self.data)
    
    def _quick(self,start,end):
        if start<end:
            mid = self._partition(start,end)
            self._quick(start,mid-1)
            self._quick(mid+1,end)
    
    def _partition(self,start,end):
        piv = self.data[start]
        low = start+1
        high = end
        while True:
            while low<=high and piv>=self.data[low]:
                low+=1
            while low<=high and piv<self.data[high]:
                high-=1
            if low<=high:
                self.data[high],self.data[low] = self.data[low],self.data[high] 
            else:
                break
        self.data[high],self.data[start] = self.data[start],self.data[high] 
        return high
    
    def mergsort(self):
        print(self.data)
        print(self._mergSort(self.data))
        
    def _mergSort(self,data):
        if len(data)<=1:
            return data
        
        mid = len(data)//2
        left = self._mergSort(data[:mid])
        right = self._mergSort(data[mid:])

        return self._merg(left,right)
    
    def _merg(self,left,right):
        res = []
        i=j=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        res.extend(left[i:])
        res.extend(right[j:])
        return res
    
class stackTesting:
    def __init__(self,size):
        self.data = [None]*size
        self.count = 0
        self.top = 0
        pass
    
    def isEmpty(self):
        return self.count==0

    def isFull(self):
        return self.count==len(self.data)

    def getpeek(self):
        return self.data[self.top-1]

    def push(self,data):
        if not self.isFull():
            self.data[self.top]=data
            self.top+=1
            self.count+=1
            print(self.data)
        else:
            print("full")

    def pop(self):
        if not self.isEmpty():
            self.top-=1
            self.data[self.top] = None
            self.count-=1
            print(self.data)
        else:
            print('emp')

class queueTesting:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.count = 0
        self.data = [None]*4

    def isEmpty(self):
        return self.count==0

    def insert(self,ele):
        if self.count==len(self.data):
            self.resize(len(self.data)*2)
        self.data[self.rear] = ele
        self.count+=1
        self.rear = (self.rear+1)%len(self.data)
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
        
class linkedListTesting:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    class node:
        def __init__(self,data):
            self.data = data
            self.next = None
    
    def isEmpty(self):
        return self.count==0

    def trav(self):
        temp = self.head
        while temp!=None:
            print(temp.data)
            temp = temp.next

    def insertHead(self,data):
        newnode = self.node(data)
        if not self.isEmpty():
            newnode.next = self.head
            self.head = newnode
        else:
            self.head = self.tail = newnode
        self.count+=1
        
    def insertTail(self,data):
        newnode = self.node(data)
        if not self.isEmpty():
            self.tail.next = newnode
            self.tail = newnode
        else:
            self.head = self.tail = newnode
        self.count+=1
        
    def deleHead(self):
        if not self.isEmpty():
            if self.head != self.tail:
                temp = self.head
                self.head = self.head.next
                temp.next = None
            else:
                self.head=self.tail=None
        
    def deleTail(self):
        if not self.isEmpty():
            if self.head != self.tail:
                temp = self.head
                while temp.next.next !=None:
                    temp = temp.next
                temp.next=None
            else:
                self.head=self.tail=None

    def deleEle(self,key):
        if not self.isEmpty():
            if self.head.data==key:
                return self.deleHead()
            if self.tail.data==key:
                return self.deleTail()
            if self.head != self.tail:
                temp = self.head
                while temp.next.data !=key:
                    temp = temp.next
                temp.next=temp.next.next

class treeTesting:
    def __init__(self):
        self.root = None
        self.count = 0

    class Node:
        def __init__(self,data):
            self.data = data
            self.left = None
            self.right = None

    def insert(self,ele):
        self.root = self._insert(self.root,ele)

    def _insert(self,node,ele):
        if node==None:
            return self.Node(ele)
        if node.data>ele:
            node.left =  self._insert(node.left,ele)
        if node.data<ele:
            node.right =  self._insert(node.right,ele)
        return node
        
    def inorder(self):
        self._inorder(self.root)

    def postorder(self):
        self._postorder(self.root)
    
    def preorder(self):
        self._preorder(self.root)
    
    def _inorder(self,node):
        if node:
            self._inorder(node.left)
            print(node.data)
            self._inorder(node.right)

    def _preorder(self,node):
        if node:
            print(node.data)
            self._preorder(node.left)
            self._preorder(node.right)
 
    def _postorder(self,node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.data)

    def delete(self,key):
        self.root = self._delete(self.root,key)
    
    def _delete(self, root, key):
        if root is None:
            return root
        if key<root.data:
            root.left = self._delete(root.left,key)
        if key>root.data:
            root.right = self._delete(root.right,key)
        else:
            if root.right is None and root.left is None:
                return None
            elif root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            
            successor = self._min_value_node(root.right)
            root.data = successor.data
            root.right = self._delete(root.right,key)
        return root      

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current