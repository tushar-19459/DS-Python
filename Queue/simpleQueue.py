class fixQueue:
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
            print(self.data)
        else:
            print(" full ")
    
    def dequeue(self):
        if not self.isEmpty():
            self.data[self.front] = None
            self.count -= 1
            self.front = (self.front+1)%self.size
            print(self.data)
        else:
            print(" empty ")

    
class infQueue:
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

        print(self.data)
    
    def dequeue(self):
        if  self.isEmpty():
            print(" empty ")
        else:
            if self.count <= len(self.data)//2 :
                self.rear = len(self.data)//2
                print('rear ',self.rear)
                self.resize(len(self.data)//2)
            self.data[self.front] = None
            self.front = (self.front+1)%len(self.data)
            self.count -= 1
        print(self.data)
