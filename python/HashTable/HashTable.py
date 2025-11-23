import numpy as np
class HashTable:
    class node:
        def __init__(self,id,name):
            self.id = id
            self.name = name
            self.next = None

    def __init__(self):
        self.hashTable_size = 11
        self.p = 13
        self.a = np.random.randint(1,self.p-1)
        self.b = np.random.randint(0,self.p-1)
        self.hashTable = [None]*self.hashTable_size
    
    def _hash_(self,id):
        code = 0
        data = str(id)
        for i in data:
            code = i<<5
            code = code+ord(i)
        return code

    def _compresstion_(self,code):
        return (((code*self.a+self.b)%self.p)%self.hashTable_size)
    
    def hash_function(self,id):
        code = self._hash_(id)
        bucket = self._compresstion_(code)
        return bucket

    def is_member(self,id):
        bucket = self.hash_function(id)
        current = self.hashTable[bucket]
        while current!=None:
            if current.id == id:
                return True
            else:
                current = current.next
        return False
    
    def insert(self,id,name):
        if not self.is_member(id):
            bucket = self.hash_function(id)
            new_node = self.node(id,name)
            new_node.next = self.hashTable[bucket]
            self.hashTable[bucket] = new_node
