# 1 class for 1th question 
class InfStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def push(self, ele):
        self.data.append(ele)

    def isEmpty(self):
        return len(self.data) == 0

    def peek(self):
        if len(self.data) != 0:
            return self.data[-1]
        else:
            return self.data

    def pop(self):
        if not self.isEmpty():
            return self.data.pop()


# 2 class for 2th question 
class simpleFixStack:
    def __init__(self, size):
        self.data = [None]*size
        self.top = 0
        self.count = 0

    def size(self):
        return self.top

    def push(self, ele):
        if not self.isFull():
            self.data[self.top] = ele
            self.top += 1
            self.count += 1
        else:
            return None

    def isFull(self):
        return self.top == len(self.data)

    def isEmpty(self):
        return self.count == 0

    def peek(self):
        return self.data[self.top-1]

    def pop(self):
        if not self.isEmpty():

            self.top -= 1
            self.count -= 1
            data = self.data[self.top]
            self.data[self.top] = None
            return data
        else:
            return None


# 3 class for 3th question 
class StackReverse:
    def __init__(self):
        self.data = []
        self.top = 0

    def push(self, ele):
        self.data.append(ele)
        self.top += 1

    def isEmpty(self):
        return len(self.data) == 0

    def pop(self):
        if not self.isEmpty():
            self.data.pop()

    def stkRev(self):
        text = ""
        while (len(self.data) != 0):
            text += self.data.pop()
            text += " "
        return text.strip()

    def checkParentheses(self, data):
        for i in data:
            if i == '(':
                self.push(i)
            elif i == ')':
                if not self.isEmpty():
                    self.pop()

        return len(self.data) == 0


# 4 class for 4th question 
class parentheses:
    def __init__(self):
        self.data = []
        self.top = 0

    def push(self, ele):
        self.data.append(ele)
        self.top += 1

    def isEmpty(self):
        return len(self.data) == 0

    def pop(self):
        if not self.isEmpty():
            self.data.pop()

    def checkParentheses(self, data):
        for i in data:
            if i == '(' or i == '[' or i=='{' or i=='<':
                self.push(i)
            elif i == ')' or i == ']' or i=='}' or i=='>':
                if not self.isEmpty():
                    self.pop()

        return len(self.data) == 0


# 5 class for 5th question 
class HtmlTags:
    def __init__(self):
        self.data = []
        self.top = 0

    def push(self, ele):
        self.data.append(ele)
        self.top += 1

    def pop(self):
        if not self.isEmpty():
            self.data.pop()

    def isEmpty(self):
        return len(self.data) == 0

    def testTag(self, prop):
        for tag in prop:
            if tag[0:2] != "</":
                self.push(tag)
            else:
                if not self.isEmpty():
                    self.pop()
        return len(self.data) == 0
    

# 6 class for 6th question 
class Signature:
    def __init__(self):
        self.S = []
        self.T = []
        self.top = 0

    def push(self, ele):
        self.S.append(ele)
        self.top += 1

    def pop(self):
        if not self.isEmpty():
            self.S.pop()

    def isEmpty(self):
        return len(self.data) == 0

    def Signature_opertaion(self):
        Temp = []
        while len(self.S) != 0:
            Temp.append(self.S.pop())
        while len(Temp) != 0:
            self.T.append(Temp.pop())

    def getT(self):
        return self.T

    def getS(self):
        return self.S


# 7 class for 7th question 
class ForwardBack:
    def __init__(self):
        self.data = ['c:Home']

    def size(self):
        return len(self.data)

    def GoTo(self, ele):
        self.data.append(ele)

    def isEmpty(self):
        return len(self.data) == 1

    def CurrentDir(self):
        return "/".join(self.data)

    def GoBack(self):
        if not self.isEmpty():
            return self.data.pop()


# 8 class for 8th question 
class HtmlTagsWithAttributes:
    def __init__(self):
        self.data = []

    def push(self, tags):
        try:
            for item in tags:
                if '<' in item and '</' not in item and "meta" not in item:
                    self.data.append(item)
                elif '</' in item :
                    self.data.pop()
                print(self.data)
            return self.isEmpty()
        except:
            return self.isEmpty()

    def isEmpty(self):
        return len(self.data) == 0

    def peek(self):
        if len(self.data) != 0:
            return self.data[-1]