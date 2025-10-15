from simpleQueue import FixedQueue,FlexyQueue ,SimpleQueue ,SatckUsingQueue,Rotate,QueueUsingStack
#1 Implement “Simple Queue” using list data structure.
def testsimpleQueue():
    queue = SimpleQueue()
    assert queue.isEmpty() == True
    assert queue.enqueue(10) == [10]
    assert queue.enqueue(20) == [10,20]
    assert queue.enqueue(30) == [10,20,30]
    assert queue.dequeue() == [20,30]
    assert queue.dequeue() == [30]
    assert queue.dequeue() == []
# testsimpleQueue()

#2 Modify Q1 such that Simple Queue can contain limited amount of elements.
def testFixedQueue():
    queue = FixedQueue(5)
    assert queue.enqueue(1)== [1,None,None,None,None]
    assert queue.enqueue(2)== [1,2,None,None,None]
    assert queue.enqueue(3)== [1,2,3,None,None]
    assert queue.enqueue(4)== [1,2,3,4,None]
    assert queue.enqueue(5)== [1,2,3,4,5]
    assert queue.dequeue()== [None,2,3,4,5]
    assert queue.enqueue(6)== [6,2,3,4,5]
    assert queue.dequeue()== [6,None,3,4,5]
    assert queue.dequeue()== [6,None,None,4,5]
    assert queue.dequeue()== [6,None,None,None,5]
    assert queue.dequeue()== [6,None,None,None,None]
    assert queue.dequeue()== [None,None,None,None,None]
# testFixedQueue()

#3 Implement “FlexiQueue” with capacity to expand and shrunk based on elements to be added or deleted.
def testflexyQueue():
    queue = FlexyQueue()
    assert queue.enqueue(1) == [1, None] 
    assert queue.enqueue(2) == [1, 2]
    assert queue.enqueue(3) == [1, 2, 3, None] 
    assert queue.enqueue(4) == [1, 2, 3, 4]
    assert queue.enqueue(5) == [1, 2, 3, 4, 5, None, None, None] 
    assert queue.dequeue()  == [None, 2, 3, 4, 5, None, None, None]
    assert queue.enqueue(6) == [None, 2, 3, 4, 5, 6, None, None] 
    assert queue.enqueue(6) == [None, 2, 3, 4, 5, 6, 6, None] 
    assert queue.enqueue(6) == [None, 2, 3, 4, 5, 6, 6, 6]
    assert queue.enqueue(6) == [6, 2, 3, 4, 5, 6, 6, 6]
    assert queue.enqueue(7) == [2, 3, 4, 5, 6, 6, 6, 6, 7, None, None, None, None, None, None, None]
    assert queue.dequeue()  == [None, 3, 4, 5, 6, 6, 6, 6, 7, None, None, None, None, None, None, None]
    assert queue.dequeue()  == [None, 4, 5, 6, 6, 6, 6, 7]
    assert queue.dequeue()  == [None, None, 5, 6, 6, 6, 6, 7]
    assert queue.dequeue()  == [None, None, None, 6, 6, 6, 6, 7]
    assert queue.dequeue()  == [None, None, None, None, 6, 6, 6, 7]
    assert queue.dequeue()  == [None, 6, 6, 7]
    assert queue.dequeue()  == [None, None, 6, 7]
    assert queue.dequeue()  == [None, 7]
    assert queue.dequeue()  == [None]
    assert queue.dequeue()  == [None]
    assert queue.dequeue()  == [None]
    assert queue.dequeue()  == [None] 
# testflexyQueue()

#4 Implement Stack using two Queues
def testSatckUsingQueue():
    stack = SatckUsingQueue(5)
    assert stack.enqueue(10) == [10,None,None,None,None]
    assert stack.enqueue(20) ==[10,20,None,None,None]
    assert stack.enqueue(30) ==[10,20,30,None,None]
    assert stack.enqueue(40) ==[10,20,30,40,None]
    assert stack.enqueue(50) ==[10,20,30,40,50]
    assert stack.enqueue(60) =="overflow"
    assert stack.pop() == 50
    assert stack.pop() == 40
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.pop() == "Empty"
    assert stack.enqueue(10) == [10,None,None,None,None]
    assert stack.enqueue(10) == [10,10,None,None,None]
# testSatckUsingQueue()

#5 Implement Queue using two Stacks
def testqueueUsingStack():
    stack = QueueUsingStack(5)
    assert stack.push(10) ==[10, None, None, None, None]
    stack.push(20) ==[10, 20, None, None, None]
    stack.push(30) == [10, 20, 30, None, None]
    stack.push(40) == [10, 20, 30, 40, None]
    stack.push(50) == [10, 20, 30, 40, 50]
    assert stack.pop() == 50
    assert stack.pop() == 40
    assert stack.dequeue() == [20, 30, None, None, None]
    assert stack.dequeue() == [30, None,None, None, None]
    assert stack.pop() == 30
    assert stack.dequeue() == [None, None,None, None, None]
# testqueueUsingStack()

#6 Assume that we have Queue with some elements. Write method rotate() which added the existing elements in the reverse order.
def testrotate():
    queue = Rotate(5)
    assert queue.enqueue(1) == [1,None,None,None,None]
    assert queue.enqueue(2) == [1,2,None,None,None]
    assert queue.enqueue(3) == [1,2,3,None,None]
    assert queue.enqueue(4) == [1,2,3,4,None]
    assert queue.enqueue(5) == [1,2,3,4,5]
    assert queue.rotateEle() == [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    assert queue.dequeue() == [None, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    assert queue.enqueue(11) == [11, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    assert queue.enqueue(11) == "full"
    assert queue.dequeue() == [11, None, 3, 4, 5, 5, 4, 3, 2, 1]
# testrotate()

#7 Implement findMax() method, which return the maximum value of element present in the queue. After finding maximum element, queue content should be same as original.
def testMax():
    queue = SimpleQueue()
    queue.enqueue(21)
    queue.enqueue(1)
    queue.enqueue(40)
    queue.enqueue(34)
    queue.enqueue(22)
    queue.enqueue(11)
    queue.enqueue(2)
    assert queue.findMax() == 40
# testMax()

