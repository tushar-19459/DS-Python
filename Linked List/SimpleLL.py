import math
class LinkeList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    class Node:
        def __init__(self,ele):
            self.data = ele
            self.next = None

    def addAtHead(self,ele):
        newNode = self.Node(ele)
        if not self.isEmpty():
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode
            self.tail = newNode
        self.count +=1

    def addAtTail(self,ele):
        newNode = self.Node(ele) 
        if not self.isEmpty():
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode
        self.count +=1
          
    def getLL(self):
        if not self.isEmpty():
            temp = self.head
            print("linkedList : ")
            while temp != None:
                print(temp.data,end=" ")
                temp = temp.next
        else:
            print(None)
        # return self.count
        print()
    
    def isEmpty(self):
        return self.count==0
    
    def getLen(self):
        return self.count

    def getNoOfEle(self):
        return self.count

    def search(self,key):
        if not self.isEmpty():
            temp = self.head
            count = 0
            while temp != None:
                if temp.data == key:
                    return count 
                count+=1
                temp = temp.next
        return -1

    def deleteAtHead(self):
        if not self.isEmpty():
            data = self.head.data
            self.head = self.head.next
            self.count-=1
            return data     
    
    def deleteAtTail(self):
        if self.getLen() == 1:
            self.tail = None
            self.head = None
            self.count = 0

        if not self.isEmpty():
            temp = self.head
            data = self.tail.data
            while temp.next.data != data:
                temp = temp.next
            self.tail = temp
            self.tail.next = None
            self.count -=1
            return data
        
    def addAfterEle(self,key,ele):
        if not self.isEmpty():
            temp = self.head
            key_ele_address = None
            while temp != None:
                if temp.data == key:
                    key_ele_address = temp
                    break
                temp = temp.next
            if key_ele_address != None:
                if key_ele_address.next!=None: 
                    new_node = self.Node(ele)
                    new_node.next = key_ele_address.next
                    key_ele_address.next = new_node
                    self.count+=1
                else:
                    self.addAtTail(ele)
                return
        return -1

    def DeleteAfterEle(self,key):
        if not self.isEmpty():
            temp = self.head
            key_ele_address = None
            while temp != None:
                if temp.data == key:
                    key_ele_address = temp
                    break
                temp = temp.next
            to_be_deleted = temp.next
            if key_ele_address != None:
                if to_be_deleted.next != None:
                    key_ele_address.next = to_be_deleted.next                
                    self.count-=1
                    # self.getLL()
                else:
                    self.deleteAtTail()
                return
        return -1
    
    def getTail(self):
        return self.tail
    
    def getHead(self):
        return self.head

    def genCommenLinkedList(self,ll1_head,ll2_head):
        data1 = []
        data2 = []
        equal = []
        temp = ll1_head
        while temp != None:
            data1.append(temp.data)
            temp = temp.next
        temp = ll2_head
        while temp != None:
            data2.append(temp.data)
            temp = temp.next
        for i in data1:
            for j in data2:
                if i==j:
                    equal.append(i)
        print(equal)

        if len(equal)!=0:
            eq_ll = LinkeList()
            for i in range(len(equal)):
                eq_ll.addAtTail(equal[i])
            eq_ll.getLL()

    def sumoOfLastN(self,n):
        index = self.count-n
        sum=0
        count=1
        if not self.isEmpty():
            temp = self.head
            while temp != None:
                if count>index:
                    sum+=temp.data                     
                count+=1
                temp = temp.next
        return sum
    
        
    
    def splitLL(self):
        tempHead = self.getHead()
        temp = self.getLen()
        ll1 = LinkeList()
        ll2 = LinkeList()
        while temp!=0:
            data  = tempHead.data
            if temp%2==0:
                ll1.addAtTail(data)
            else:
                ll2.addAtTail(data)
            tempHead = tempHead.next
            temp-=1
        print("original Linked List ")
        self.getLL()
        print("Linked List 1 ")
        ll1.getLL()
        print("Linked List 2 ")
        ll2.getLL()

    def isPalindrome(self):
        while self.getLen()>1 :
            data2 = self.deleteAtTail()
            data1 = self.deleteAtHead()
            if data1!=data2:
                return False
        return True
    
    def reverseLL(self):
        tempData = []
        if not self.isEmpty():
            temp = self.head
            while temp != None:
                tempData.append(temp.data)
                temp = temp.next
        print(tempData)
        rLinked = LinkeList()
        for i in tempData[::-1]:
            rLinked.addAtTail(i)
        rLinked.getLL()

    def removeDublicates(self):
        i = self.getHead()
        while i !=None:
            j = i.next
            while j != None:
                if i!=j and i.data==j.data:
                    self.DeleteAfterEle(pre)
                pre = i.data
                j = j.next
            i= i.next
    
    def getMid(self):
        mid = int(self.getLen()/2)
        for i in range(mid):
            self.deleteAtHead()
        return self.deleteAtHead()
    
    def removeOddFromCircular(self):
        if self.head is None:
            return
        
        while self.head and self.head.data % 2 != 0:
            if self.head == self.tail:  
                self.head = None
                self.tail = None
                self.count = 0
                return
            self.head = self.head.next
            self.tail.next = self.head
            self.count -= 1

        curr = self.head
        while curr.next != self.head:
            if curr.next.data % 2 != 0:
                if curr.next == self.tail:  
                    self.tail = curr
                curr.next = curr.next.next
                self.count -= 1
            else:
                curr = curr.next


    def displayCircular(self):
        if self.head is None:
            print("List is empty")
            return
        
        temp = self.head
        print("Circular Linked List:", end=" ")
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:  
                break
        print()
