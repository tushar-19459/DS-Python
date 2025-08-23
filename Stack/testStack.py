from stack import simpleFixStack, StackReverse, Signature, HtmlTags, parentheses, InfStack,ForwardBack,HtmlTagsWithAttributes

file = open('./testing.txt', mode='r')
htmlFile = open('./index.html', mode='r')
text = file.read()
data = text.split(" ")


htmlFileAttributes = open('./testing.html', mode='r')
tags = htmlFile.read()
Attributes= htmlFileAttributes.read().split('\n')
Attributes = [item.strip() for item in Attributes ]

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
# test_InfStack()


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
# test_Fixstack()


def test_rev_stack():
    stack = StackReverse()
    for i in data:
        stack.push(i)
    value = stack.stkRev()
    rev_text = " ".join(data[::-1])
    print(text)
    print(value)
    assert value == rev_text
# test_rev_stack()


def testParentheses():
    stack = parentheses()
    chars = list(text)
    assert stack.checkParentheses(chars) == True
# testParentheses()


def testSignature():
    stack = Signature()
    for i in data:
        stack.push(i)

    print(stack.getS())
    stack.Signature_opertaion()
    print(stack.getT())
# testSignature()


def testHtml():
    stack = HtmlTags()
    data = tags.replace('\n', " ").split(" ")
    # print(data)
    data = [item for item in data if item != ""]
    # data = [item[1:-1] for item in data ]
    # print(data[3][0:1])
    print(stack.testTag(data))
# testHtml()


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
# test_Forwardand_Back()

def test_att():
    stack = HtmlTagsWithAttributes()
    print(stack.push(Attributes))
test_att()