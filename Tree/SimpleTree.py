class SimpleTree:
    def __init__(self):
        self.root = None
        self.count=0
        
    class Node:
        def __init__(self,data):
            self.ele = data
            self.left= None
            self.right= None
    
    def isEmpty(self):
        return self.count==0
    
    def getCount(self):
        return self.count

    def insert(self,data):
        current = par_naode = self.root
        while current != None and current.ele!=data:
            par_naode = current
            if data < current.ele:
                current = current.left
            else:
                current = current.right
            
        if current == None:
            node = self.Node(data)
            if par_naode !=None:
                if data<par_naode.ele:
                    par_naode.left = node
                else:
                    par_naode.right = node
            else:
                self.root = node
            self.count+=1

    def travers(self):
        print('pretorder')
        self.preorder(self.root)
        print('inorder')
        self.inorder(self.root)
        print('postorder')
        self.postorder(self.root)

    def inorder(self,node):
        if node!=None:
            self.inorder(node.left)
            print(node.ele)
            self.inorder(node.right)
    
    def postorder(self,node):
        if node!=None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.ele)
    
    def preorder(self,node):
        if node!=None:
            self.preorder(node.left)
            self.preorder(node.right)
            print(node.ele)

    def isMember(self,data):
        node = self.root
        while node != None:
            if data == node.ele:
                return True
            if data<node.ele:
                node = node.left
            else:
                node = node.right
        return False
    
    def deleteNode(self,key):
        if not self.isEmpty():
            self.root = self._deleteNode_(self.root,key)
    
    def _deleteNode_(self,node,key):
        if node is None:
            return None
    
        if node.ele>key:
            node.left = self._deleteNode_(node.left,key)
        elif node.ele<key:
            node.right = self._deleteNode_(node.right,key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                succ = self.getMin(node.right)
                node.ele = succ.ele
                node.right = self._deleteNode_(node.right,succ.ele)
        return node

    def getMin(self,node):
        current = node
        while current.left is not None:
            current = current.left 
        return current