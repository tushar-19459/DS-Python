class SimpleQueue:
    def __init__(self):
        self.data = []
    
    def isEmpty(self):
        return len(self.data) == 0

    def enqueue(self,ele):
        self.data.append(ele)
        return self.data
    
    def dequeue(self):
        if not self.isEmpty():
            ele = self.data[0]
            self.data = self.data[1:]
            return self.data
    
    def findMax(self):
        if not self.isEmpty():
            max = self.data[0]
            for i in range(1,len(self.data)):
                 if max < self.data[i]:
                    max = self.data[i]
            return max
    
    def get(self):
        return self.data
        
class FixedQueue:
    def __init__(self,size):
        self.size= size
        self.data = [None]*size
        self.count = 0
        self.rear = 0
        self.front = 0
    
    def isEmpty(self):
        return self.count == 0

    def enqueue(self,ele):
        if self.count != len(self.data):
            self.data[self.rear] = ele
            self.rear = (self.rear+1)%self.size
            self.count +=1
            return self.data
        else:
            print(" full ")
    
    def dequeue(self):
        if not self.isEmpty():
            self.data[self.front] = None
            self.count -= 1
            self.front = (self.front+1)%self.size
            return self.data
        else:
            print(" empty ")
    
    def findMax(self):
        if not self.isEmpty():
            max = self.data[0]
            for i in range(1,len(self.data)):
                 if max < self.data[i]:
                    max = self.data[i]
            return max

class FlexyQueue:
    def __init__(self):
        self.size = 2
        self.data = [None]*self.size
        self.count = 0
        self.rear = 0
        self.front = 0
    
    def isEmpty(self):
        return self.count == 0
    
    def resize(self,size):
        newdata = [None]*size
        for i in range(self.count):
            newdata[i] = self.data[self.front]
            self.front = (self.front+1)%len(self.data)
        self.front = 0
        self.rear = len(self.data)
        self.data = newdata
        pass

    def enqueue(self,ele):
        if self.count == len(self.data):
            self.resize(len(self.data)*2)
            pass
        self.data[self.rear] = ele
        self.rear = (self.rear+1)%len(self.data)
        self.count+=1

        return self.data
    
    def dequeue(self):
        if  self.isEmpty():
            pass
            # print(" empty ")
        else:
            if self.count <= len(self.data)//2 :
                self.rear = len(self.data)//2
                self.resize(len(self.data)//2)
            self.data[self.front] = None
            self.front = (self.front+1)%len(self.data)
            self.count -= 1
        return self.data

class SatckUsingQueue:
    def __init__(self,size):
        self.size= size
        self.data = [None]*size
        self.count = 0
        self.rear = 0
        self.front = 0

        self.tempdata = [None]*size
        self.temprear = 0

    def isEmpty(self):
        return self.count == 0

    def enqueue(self,ele):
        if self.count != len(self.data):
            self.data[self.rear] = ele
            self.rear = (self.rear+1)%self.size
            self.count +=1
            return self.data
        else:
            return "overflow"
    
    def dequeue(self):
        if not self.isEmpty():
            ele = self.data[self.front]  
            self.data[self.front] = None
            self.count -= 1
            self.front = (self.front+1)%self.size
            return ele
        else:
            print(" empty ")

    def pop(self):
        if not self.isEmpty():
            front = self.front
            n = self.count
            pop = None
            for i in range(n-1):
                self.tempdata[i] = self.dequeue()
            pop = self.dequeue()
            self.rear = self.count % self.size
            self.data = self.tempdata
            self.tempdata = [None]*self.size
            self.count = n - 1
            self.front = front
            return pop
        else:
            return "Empty"
        
class Rotate:
    def __init__(self,size):
        self.size= size
        self.data = [None]*size
        self.count = 0
        self.rear = 0
        self.front = 0
    
    def isEmpty(self):
        return self.count == 0

    def enqueue(self,ele):
        if self.count != len(self.data):
            self.data[self.rear] = ele
            self.rear = (self.rear+1)%self.size
            self.count +=1
            return self.data
        else:
            return "full"
    
    def dequeue(self):
        if not self.isEmpty():
            self.data[self.front] = None
            self.count -= 1
            self.front = (self.front+1)%self.size
            return self.data
        else:
            return "empty"
    
    def findMax(self):
        if not self.isEmpty():
            max = self.data[0]
            for i in range(1,len(self.data)):
                 if max < self.data[i]:
                    max = self.data[i]
            return max
        
    def rotateEle(self):
        temp = self.data[:]
        self.data +=temp[::-1]
        self.size = self.size*2
        self.count = self.count*2
        self.rear = self.rear*2%self.size
        return self.data

class QueueUsingStack:
    def __init__(self,size):
        self.data = [None]*size
        self.top = 0
        self.count = 0
    
    def push(self,ele):
        if not self.isfull():
            self.data[self.top] = ele
            self.top += 1
            self.count +=1
            return self.data
        
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            self.count -=1
            ele = self.data[self.top]
            self.data[self.top] = None
            return ele
    
    def dequeue(self):
        if not self.isEmpty():
            temp = []
            n = self.count 
            while n!=1:
                temp.append(self.pop())
                n -=1
            self.pop()
            while len(temp) !=0:
                self.push(temp.pop())
        return self.data
        

    def isfull(self):
        return self.top == len(self.data)
    
    def isEmpty(self):
        return self.top == 0