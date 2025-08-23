class simpleQueue:
    def __init__(self,size):
        self.data = [None]*size
        self.font = 0
        self.count = 0

    def getCount(self):
        return self.count
    
    def is_empty(self):
        return self.count==0
    
    def get_first(self):
        if not self.is_empty(self):
            return self.data[self.font]
        else:
            return None
        
    def enqueue(self):
        if self.count == len(self.data):
            self.resize(len)