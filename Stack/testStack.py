from stack import simpleFixStack, StackReverse, Signature, HtmlTags, parentheses, InfStack,ForwardBack,HtmlTagsWithAttributes

file = open('./testing.txt', mode='r')
htmlFile = open('./index.html', mode='r')
text = file.read()
data = text.split(" ")

htmlFileAttributes = open('./testing.html', mode='r')
tags = htmlFile.read()
Attributes= htmlFileAttributes.read().split('\n')
Attributes = [item.strip() for item in Attributes ]


# 1. Implement unlimited size stack
def test_InfStack():
    s = InfStack()
    assert s.isEmpty() == True

    s.push(10)
    assert s.isEmpty() == False
    assert s.peek() == 10
    assert s.size() == 1

    assert s.pop() == 10
    assert s.isEmpty() == True
    assert s.size() == 0

    for i in range(100000):
        s.push(i)

    assert s.size() == 100000
    assert s.peek() == 99999
    assert s.isEmpty() == False

    for i in reversed(range(100000)):
        assert s.pop() == i

    assert s.isEmpty() == True
    assert s.size() == 0
test_InfStack()


#2. Implement limited size Stack
def test_Fixstack():
    s = simpleFixStack(3)

    assert s.isEmpty() == True
    assert s.isFull() == False
    assert s.top == 0

    s.push(10)
    s.push(20)
    assert s.peek() == 20
    assert s.top == 2
    assert s.isEmpty() == False

    s.push(30)
    assert s.isFull() == True
    assert s.peek() == 30

    assert s.pop() == 30
    assert s.pop() == 20
    assert s.peek() == 10
    assert s.top == 1

    assert s.pop() == 10
    assert s.isEmpty() == True
test_Fixstack()


# 3. Reverse the content of file using Stack
def test_rev_stack():
    stack = StackReverse()
    for i in data:
        stack.push(i)
    value = stack.stkRev()
    rev_text = " ".join(data[::-1]).strip()
    assert value == rev_text
test_rev_stack()


# 4. Match the parentheses using Stack
def testParentheses():
    stack = parentheses()
    chars = list(text)
    assert stack.checkParentheses(chars) == True 
testParentheses()


# 5. Match the tags in HTML file using Stack
def testHtml():
    stack = HtmlTags()
    data = tags.replace('\n', " ").split(" ")
    data = [item for item in data if item != ""]
    assert stack.testTag(data) == True #returns true if all the html tags are closed correcty
testHtml()


# 6. Implement a function with signature transfer(S,T). This function transfers all elements from Stack S to Stack T. The sequence of elements in T should be same as that of S.
def testSignature():
    stack = Signature()
    for i in data:
        stack.push(i)

    # print(stack.getS())
    stack.Signature_opertaion()
    # print(stack.getT())
testSignature()


# 7. Implement “Forward” and “Back” buttons of browser using Stacks. Elements need to be stored are URLs.
def test_Forwardand_Back():
    stack = ForwardBack()
    assert stack.CurrentDir() == "c:Home"
    stack.GoTo("documents")
    assert stack.CurrentDir() == "c:Home/documents"
    stack.GoTo("Program")
    assert stack.CurrentDir() == "c:Home/documents/Program"
    stack.GoTo("java")
    assert stack.CurrentDir() == "c:Home/documents/Program/java"
    stack.GoBack()
    assert stack.CurrentDir() == "c:Home/documents/Program"
    stack.GoBack()
    assert stack.CurrentDir() == "c:Home/documents"
    stack.GoBack()
    assert stack.CurrentDir() == "c:Home"
    stack.GoBack()
    assert stack.CurrentDir() == "c:Home"
test_Forwardand_Back()


# 8. Modify Q5 such that HTML tags may contain attributes along with tag name.
def test_att():
    stack = HtmlTagsWithAttributes()
    assert stack.push(Attributes) == True #returns true if all the html tags are closed correcty
test_att()