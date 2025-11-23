import numpy as np

class Hashhash_Table:
    class node:
        def __init__(self,id,name):
            self.id = id
            self.name = name
            self.next = None
            
    def __init__(self):
        self.hash_table_size = 11
        self.hash_table = [None]*self.hash_table_size
        self.p = 13
        self.a = np.random(1,self.p-1)
        self.b = np.random(0,self.p-1)
        
    def _hash_(self,id):
        code = 0
        id = str(id)
        for ch in id:
            code = code<<5
            self.code = code+ord(ch)
        return code

    def _compress_(self,code):
        return (((code*self.a+self.b)%self.p)%self.hash_table_size)

    def hashFunction(self,id):
        code = self._hash_(id)
        bucket = self._compress_(code)
        return bucket 

    def isMenmber(self,id):
        bucket = self.hashFunction(id)
        current = self.hash_table[bucket]
        while current!=None:
            if current.id == id:
                return True
            else:
                current = current.next
        return False

    def insert(self,id,name):
        if not self.isMenmber(id):
            bucket = self.hashFunction(id)
            new_node = self.node(id,name)
            new_node.next = self.hash_table[bucket]
            self.hash_table[bucket] = new_node