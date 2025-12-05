class SimpleStack:
    def __init__(self):
        self.val = [None]*5
        self.top=0
        self.count=0
    
    def isFull(self):
        return self.top==len(self.val)
    
    def isEmpty(self):
        return self.count==0
    
    def push(self,val):
        if not self.isFull():
            self.val[self.top]=val
            self.top+=1
            self.count+=1

    def pop(self):
        if not self.isEmpty():
            self.top -= 1 
            self.count-= 1 
            self.val[self.top]=None

    def getstack(self):
        return self.val   

class SimpleQueue:
    def __init__(self):
        self.val=[None]*5
        self.front = 0
        self.rear= 0
        self.count=0
    
    def isEmpty(self):
        return self.count==0
    
    def isFull(self):
        return self.count==len(self.val)
    
    def Enqueue(self,val):
        if not self.isFull():
            self.val[self.rear]=val
            self.count+=1
            self.rear+=1
    
    def Dequeue(self):
        if not self.isEmpty():
            self.val[self.front]=None
            self.count-=1
            self.front+=1

    def getQueue(self):
        return self.val  

class FlexQueue:
    def __init__(self):
        self.val = [None]*5
        self.front = 0
        self.rear = 0
        self.count=0

    def isEmpty(self):
        return self.count==0
    
    def Enqueue(self,val):
        if self.count==len(self.val):
            self.resize(len(self.val)*2)
        self.val[self.rear]=val
        self.count+=1
        self.rear=(self.rear+1)%len(self.val)

    def Dequeue(self):
        if not self.isEmpty():
            if self.count<len(self.val)/2:
                self.resize(len(self.val)//2)
            
            self.val[self.front]=None
            self.front+=(self.front+1)%len(self.val)
            self.count-=1

    def getQueue(self):
        return self.val
    
    def resize(self,size):
        newval = [None]*size
        for i in range(self.count):
            newval[i]=self.val[(self.front+i)%len(self.val)]
        self.val = newval
        self.front=0
        self.rear=self.count

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    
    class Node:
        def __init__(self,val):
            self.val=val
            self.next=None
    
    def isEmpty(self):
        return self.count==0
    
    def insertAtTail(self,val):
        newnode = self.Node(val)
        if not self.isEmpty():
            self.tail.next = newnode
            self.tail = newnode
        else:
            self.head=newnode
            self.tail=newnode
        self.count+=1

    def insertAtHead(self,val):
        newnode = self.Node(val)
        if not self.isEmpty():
            newnode.next = self.head 
            self.head = newnode
        else:
            self.head=newnode
            self.tail=newnode
        self.count+=1

    def deletAtHead(self):
        if not self.isEmpty():
            temp = self.head
            self.head = self.head.next
            temp.next=None
            self.count-=1
        else:
            self.head=None
            self.tail=None
            self.count=0

    def deletAtTail(self):
        if not self.isEmpty():
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next=None
            self.tail = temp
            self.count-=1
        else:
            self.head=None
            self.tail=None
            self.count=0

    def isAMember(self,key):
        if not self.isEmpty():
            temp = self.head
            while temp.val!=key:
                temp = temp.next
            if temp.val==key:
                return True
            else:
                return False
                  
    def deletAfterValue(self,key):
        temp = self.head
        while temp.next.val != key and not self.isEmpty():
            temp = temp.next
        
        if temp.next.val == key:
            print(temp.val)
            temp.next = temp.next.next

    def deletBeforeValue(self,key):
        temp = temp1 = self.head
        while temp.next.val != key and not self.isEmpty():
            temp1 = temp
            temp = temp.next
        
        if temp.next.val == key:
            temp1.next = temp.next

        
    def getll(self):
        temp = self.head
        while temp!=None:
            print(temp.val,end="")
            temp = temp.next
        print()
        
class BinaryTree:
    def __init__(self):
        self.root = None
        self.count=0
    
    class Node:
        def __init__(self,val):
            self.val = val
            self.left = None
            self.right = None

    def isEmpty(self):
        return self.root == None
    
    def insert(self,val):
        self.root=self._insert_(self.root,val)
        
    def _insert_(self,node,val):
        if node==None:
            return self.Node(val)
        if node.val>val:
            node.left = self._insert_(node.left,val)
        
        if node.val<val:
            node.right = self._insert_(node.right,val)

        return node

    def inorder(self):
        self._inorder_(self.root)
    
    def _inorder_(self,node):
        if node:
            print(node.val)
            self._inorder_(node.left)
            self._inorder_(node.right)
    
    def search(self,ele):
        temp = self.root
        while temp!=None:
            if temp.val == ele:
                return True
            elif ele<temp.val:
                temp=temp.left
            else:
                temp=temp.right
        return False
        
    def delete(self,key):
        self._delete_(self.root,key)
    
    def _delete_(self,node,key):
        if node is None:
            return None
        
        if node.val>key:
            node.left = self._delete_(node.left,key)
        elif node.val<key:
            node.right = self._delete_(node.right,key)
        else:
            if node.left is None and node.right is None:
                return node
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            sucessor = self.min_val(node.right)
            node.val = sucessor.val
            node.rigth = self._delete_(node.right,key)
        return node 

    def min_val(self,node):
        current = node
        while current is not None:
            current = current.left
        return current

class Sorting:
    def __init__(self,data):
        self.data = data
    
    def swape(self,j,i):
        self.data[j],self.data[i]=self.data[i],self.data[j]
    
    def bubleSort(self):
        for i in range(len(self.data)):
            for j in range(len(self.data)-i-1):
                if self.data[j]>self.data[j+1]:
                    self.swape(j,j+1)
        print(self.data)

    def selectionSort(self):
        for i in range(len(self.data)):
            min = i
            for j in range(i+1,len(self.data)):
                if self.data[j]<self.data[min]:
                    min=j
            self.swape(i,min)
        print(self.data)

    def insertionSort(self):
        for i in range(1,len(self.data)):
            temp = self.data[i]
            j=i-1
            while j>=0 and temp<self.data[j]:
                self.data[j+1]=self.data[j]
                j-=1
            self.data[j+1]=temp
        print(self.data)
    
    def quickSort(self):
        self._quickSort_(0,len(self.data)-1)
        print(self.data)

    def _quickSort_(self,start,end):
        if start<end:
            mid = self._partition_(start,end)
            self._quickSort_(start,mid-1)
            self._quickSort_(mid+1,end)
    
    def _partition_(self,start,end):
        piv = start 
        low = start+1
        high = end    
        while True:
            if low<=high and self.data[low]<=self.data[piv]:
                low+=1
            if low<=high and self.data[high]>self.data[piv]:
                high-=1
            if low<=high:
                self.data[low],self.data[high] = self.data[high],self.data[low] 
            else:
                break
        self.data[high],self.data[piv] = self.data[piv],self.data[high] 
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
    
import numpy as np

class HashTable:
    def __init__(self):
        self.p = 13
        self.a = np.random.randint(1,self.p-1)
        self.b = np.random.randint(0,self.p-1)
        self.size = 11
        self.table = [None]*self.size
    
    class Node:
        def __init__(self,name):
            self.id = id
            self.name = name
    
    def _hash_(self,id):
        id = str(id)
        code = 0
        for i in id:
            code = code<<5
            code = code+ord(i) 
        return code
    
    def _compress_(self,code):
        return (((code*self.a)+self.b)%self.p)%self.size

    def hashFunction(self,id):
        code = self._hash_(id)
        bucket = self._compress_(code)
        return bucket

    def isMember(self,id):
        bucket = self.hashFunction(id)
        node = self.table[bucket]
        while node != None:
            if node.id == id:
                return True
            else:
                node = node.next
        return False

    def insert(self,id,name):
        if not self.isMember(id):            
            bucket = self.hashFunction(id)
            newnode = self.Node(id,name)
            newnode.next = self.table[bucket]
            self.table[bucket] = newnode

import sys
class undirectedGraph:
    class Node:
        def __init__(self,id):
            self.id = id
            self.neighbours = {}
        
        def _addNeighbours_(self,id,weight=0):
            if not self._isNeighbour_(id):
                self.neighbours[id]=weight
        
        def _isNeighbour_(self,id):
            return id in self.neighbours.keys()
        
        def _getEdgeCost_(self,id):
            if id in self.neighbours.keys():
                return self.neighbours[id]
            else:
                return sys.maxsize
            
        def _getAllNeighbours_(self):
            return self.neighbours.keys()
        
    def __init__(self):
        self.allNodes = {}
        self.count = 0
        pass

    def addNode(self,id):
        if id not in self.allNodes.keys():
            newnode = self.Node(id)
            self.allNodes[id]=newnode
            self.count+=1
    
    def addEdge(self,fromNode,toNode,weight=0):
        if fromNode not in self.allNodes.keys():
            self.allNodes[fromNode]=self.Node(fromNode)
        if toNode not in self.allNodes.keys():
            self.allNodes[toNode]=self.Node(toNode)
        
        self.allNodes[fromNode]._addNeighbours_(toNode,weight)
        self.allNodes[toNode]._addNeighbours_(fromNode,weight)

    def getEdgeCose(self,fromNode,toNode):
        if fromNode not in self.allNodes.keys() or toNode not in self.allNodes.keys():
            return sys.maxsize
        else:
            return self.allNodes[fromNode]._getEdgeCost_(toNode)
        
    def getAllneighborus(self,id):
        if id in self.allNodes.keys():
            return self.allNodes[id]._getAllNeighbours_()
        else:
            return None
    
    def getcount(self):
        return self.count
    
    def dfs(self,start,end):
        if start not in self.allNodes.keys() or end not in self.allNodes.keys():
            return None
        
        vis = set()
        path = []
        
        def _dfs_(current):
            path.append(current)
            vis.add(current)

            if current==end:
                return True

            for i in self.getAllneighborus(current):
                if i not in vis:
                    if _dfs_(i):
                        return True
            path.pop()
            return False

        _dfs_(start)
        print(path)

    def bfs(self,start,end):
        if start not in self.allNodes.keys() or end not in self.allNodes.keys():
            return None
            
        parent ={start:None}
        vis = set([start])
        queue = [start]

        while len(queue)>0:
            current = queue.pop(0)
            for i in self.getAllneighborus(current):
                if i not in vis:
                    queue.append(i)
                    vis.add(i)
                    parent[i]=current
        
        if end not in parent.keys():
            return None
        
        path=[]
        node = end
        while node !=None:
            path.append(node)
            node = parent[node]
        print(path[::-1])
             
def testBrut(lable,text):
    a = len(text)
    b = len(lable)
    for i in range(0,a-b+1):
        j=0
        while j<b and text[i+j]==lable[j]:
            j+=1
        if j==b:
            print('found at ',i)

def binarySearch(data,key):
    low=0
    high=len(data)-1
    while low<=high:
        mid=(low+high)//2
        if data[mid]==key:
            return mid
        
        if key<data[mid]:
            high=mid-1
        else:
            low=mid+1
    return False




class Testing:
    def __init__(self,data):
        self.data = data
        self.root = None
        self.count = 0

    class Node:
        def __init__(self,data):
            self.data = data
            self.left = None
            self.right = None
        
    def isEmpty(self):
        return self.root==None
    
    def insert(self,ele):
        self.root = self._insert_(ele,self.root)

    def _insert_(self,ele,node):
        if node == None:
            return self.Node(ele)
        if ele<node.data:
            node.left = self._insert_(ele,node.left)
        if ele>node.data:
            node.right = self._insert_(ele,node.right)
        return node
    
    def isMember(self,ele):
        temp = self.root
        while temp!=None:
            if temp.data == ele:
                return True
            elif ele<temp.data:
                temp=temp.left
            else:
                temp=temp.right
        return False
    
    def inorder(self):
        self._inorder_(self.root)
        print()

    def _inorder_(self,node):
        if node==None:
            return 
        self._inorder_(node.left)
        print(node.data,end=" ")
        self._inorder_(node.right)

    def delete(self,ele):
        self.root = self._delete_(ele,self.root)
    
    def _delete_(self,ele,node):
        if node is None:
            return None
        
        if ele<node.data:
            node.left =  self._delete_(ele,node.left)
        elif ele>node.data:
            node.right =  self._delete_(ele,node.right)
        else:
            if node.left is None and node.right is None:
                return node
            if node.left is None:
                return node.right
            if node.right is None: 
                return node.left
            succesor = self.find_min(node.right)
            node.data = succesor.data
            node.right =  self._delete_(succesor.data,node.right)
        return node
    
    def find_min(self,node):
        temp = node
        while temp.left!=None:
            temp = temp.left
        return temp

    def bubleSort(self):
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)-1-i):
                if self.data[j]>self.data[j+1]:
                    self.data[j],self.data[j+1]=self.data[j+1],self.data[j]
        print(self.data)

    def selectionSort(self):
        for i in range(0,len(self.data)-1):
            min = i
            for j in range(i+1,len(self.data)):
                if self.data[min]>self.data[j]:
                    min=j        
            self.data[i],self.data[min]=self.data[min],self.data[i]
        print(self.data)

    def insertionsort(self):
        for i in range(1,len(self.data)):
            j=i-1
            temp = self.data[i]
            while j>=0 and temp<self.data[j]:
                self.data[j+1]=self.data[j]
                j-=1
            self.data[j+1]=temp
        print(self.data)

    def quickSort(self):
        self._quickSort_(0,len(self.data)-1)
        print(self.data)

    def _quickSort_(self,start,end):
        if start<end:
            mid = self._partition_(start,end)
            self._quickSort_(start,mid-1)
            self._quickSort_(mid+1,end)
    
    def _partition_(self,start,end):
        piv = start
        low = start+1
        high = end
        while True:
            if low<=high and self.data[low]<=self.data[piv]:
                low+=1
            elif low<=high and self.data[high]>self.data[piv]:
                high-=1
            elif low<=high:
                self.data[high],self.data[low] = self.data[low],self.data[high] 
            else:
                break
        
        self.data[high],self.data[piv] = self.data[piv],self.data[high] 
        return high
            
    def mergeSort(self):
        print(self._mergSort_(self.data))
        print(self.data)
    
    def _mergSort_(self,tempdata):
        if len(tempdata)<=1:
            return tempdata
        mid = len(tempdata)//2
        left = self._mergSort_(tempdata[:mid])
        right = self._mergSort_(tempdata[mid:])

        return self.merge(left,right)
    
    def merge(self,left,right):
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