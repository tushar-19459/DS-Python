import numpy as np
class Manipal_Payment:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        self.user_transactions = {}

    def isEmpty(self):
        return self.count==0

    class user:
        def __init__(self,name,phno,acno):
            self.name = name
            self.phno = phno
            self.acno = acno
            self.warnings = 0
            self.blocked = False
            self.msp_id = np.random.randint(100000)
            self.transactions = []
            self.next = None

    def register(self,name,phno,acno):
        newuser = self.user(name,phno,acno)
        if not self.isEmpty():
            self.tail.next = newuser
            self.tail = newuser
        else:
            self.head = self.tail = newuser
        self.count+=1
        self.user_transactions[newuser.msp_id] = (0,0,0) #0->debit 1->amount debited 2->transaction balence
        return newuser.msp_id

    def getuser(self,msp_id):
        temp = self.head
        while temp != None:
            if temp.msp_id == msp_id:
                return temp
            temp = temp.next

    def getAll(self):
        if not self.isEmpty():
            temp = self.head
            while temp != None:
                print(temp.name)
                temp = temp.next
    
    def credit(self,mpsid,amount):
        user = self.getuser(mpsid)
        if user:
            transaction = self.user_transactions[mpsid]
            updated_transaction = (transaction[0],transaction[1],transaction[2]+amount)
            self.user_transactions[mpsid] = updated_transaction
            user.transactions.append(amount)

    def debit(self,mpsid,amount):
        user = self.getuser(mpsid)
        transaction = self.user_transactions[mpsid]
        if not user.blocked:
            if transaction[2]>=amount and transaction[0]<5 and transaction[1]<=20000 and user.warnings==0:
                updated_transaction = (transaction[0]+1,transaction[1]+amount,transaction[2]-amount)
                self.user_transactions[mpsid] = updated_transaction
                user.transactions.append(-amount)
                print(user.transactions,updated_transaction)
            else:
                user.warnings = user.warnings+1
                print('daily limit reached')
                if user.warnings==3:
                    user.blocked=True
        else:
            print('blocked')

    def getTransaction(self,mpsid):
        transaction = self.getuser(mpsid).transactions[::-1]
        print(transaction[0:10])
        pass

    def admin_getcount(self):
        return self.count
    
    def admin_getdetail(self,mpsid):
        user = self.getuser(mpsid)
        return (user.name,user.phno,user.acno,user.msp_id)