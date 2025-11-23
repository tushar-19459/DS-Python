import sys

class Graph:
    class node:
        def __init__(self,id):
            self.id = id 
            self.neighor = {}

        def _add_neighbors(self,id,wt=0):
            if not self.is_neighbor(id) :
                self.neighor[id]=wt
        
        def is_neighbor(self,id):
            return  id in  self.neighor.keys()

        def _get_neighnor_list(self):
            return self.neighor.keys()

        def _edge_cost(self,id):
            if self.is_neighbor(id):
                return self.neighor[id]
            else:
                return sys.maxsize
    
    def __init__(self):
        self.count = 0
        self.all_node = {}

    def _is_node_(self,id):
        return id in self.all_node.keys()

    def insert_node(self,id):
        if not self._is_node_(id):
            node = self.node(id)
            self.all_node[id] = node
        self.count+=1        

    def insert_edge(self,from_node ,to_node ,wt=0):
        if not self._is_node_(from_node):
            self.insert_node(from_node)
        if not self._is_node_(to_node):
            self.insert_node(to_node)
        
        self.all_node[from_node]._add_neighbors(to_node,wt)
        self.all_node[to_node]._add_neighbors(from_node,wt)
         
    def get_count(self):
        return self.count
    
    def get_neighbors(self,id):
        return self.all_node[id]._get_neighnor_list()
    
    def get_edgeCost(self,from_node,to_node):
        return self.all_node[from_node]._edge_cost(to_node)

    def test_dfs(self,from_N,to_N):
        if not self._is_node_(from_N) or not self._is_node_(to_N):
            return None
        
        vissited = set()
        path = []

        def dfs(current):
            vissited.add(current)
            path.append(current)

            if current == to_N:
                return True
            
            for i in self.get_neighbors(current):
                if not i in vissited:
                    if dfs(i):
                        return True
            path.pop()#if lead to dead end 
            return False

        dfs(from_N)
        return path

    def test_bfs(self,start,end):
        queue = []

        def enqueu(ele):
            queue.append(ele)

        def dequeue(ele):
            queue = queue[1:]

        def bfs(start):
            pass
        

    def bfs(self,start,end):
        if not self._is_node_(start) or not self._is_node_(end):
            return None
        parent = {start:None}
        queue = [start]
        visited = set([start])
        while len(queue)>0:
            current = queue.pop(0)
            if current==end:
                break

            for i in self.get_neighbors(current):
                if not i in visited:
                    visited.add(i)
                    queue.append(i)
                    parent[i] = current 
        
        if not end in parent.keys():
            return None

        node = end
        path = []
        while node!=None:
            path.append(node)
            node = parent[node]
        return path

