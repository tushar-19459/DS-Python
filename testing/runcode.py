from testcode import SimpleStack,SimpleQueue,FlexQueue,linkedList,BinaryTree,Sorting,undirectedGraph,Testing
def testSimpleStack():
    stk = SimpleStack()
    stk.push(10)
    stk.push(20)
    stk.push(30)
    stk.push(40)
    stk.push(50)
    print(stk.getstack())
    stk.pop()
    stk.pop()
    stk.pop()
    stk.pop()
    stk.pop()
    stk.pop()
    print(stk.getstack())
# testSimpleStack()

def testSimpleQueue():
    qu = SimpleQueue()
    qu.Enqueue(10)
    qu.Enqueue(20)
    qu.Enqueue(30)
    qu.Enqueue(40)
    qu.Enqueue(50)
    print(qu.getQueue())
    qu.Dequeue()
    qu.Dequeue()
    print(qu.getQueue())
# testSimpleQueue()

def testFlexQueue():
    qu = FlexQueue()
    qu.Enqueue(10)
    qu.Enqueue(20)
    qu.Enqueue(30)
    qu.Enqueue(40)
    qu.Enqueue(50)
    qu.Enqueue(60)
    print(qu.getQueue())
    qu.Dequeue()
    qu.Dequeue()
    qu.Dequeue()
    qu.Dequeue()
    qu.Dequeue()
    print(qu.getQueue())
# testFlexQueue()

def testLinkedList():
    ll = linkedList()
    ll.insertAtTail(10)
    ll.insertAtTail(20)
    ll.insertAtTail(30)
    ll.insertAtTail(40)
    ll.insertAtTail(50)
    ll.insertAtTail(60)
    ll.getll()
    ll.deletBeforeValue(40)
    ll.getll()
# testLinkedList()

def testBinaryTree():
    tree = BinaryTree()
    data = [12,4,10,18,22,31,6,5]
    for i in data:
        tree.insert(i)
    # tree.inorder()
    # print(tree.search(6))
    tree.delete(10)
    tree.inorder()
    tree.search(10)
# testBinaryTree()

def testSort():
    data = [12,4,10,18,22,31,6,5]
    s = Sorting(data)
    # s = sorting(data)
    # s.bubleSort()
    # s.selectionSort()
    # s.insertionSort()
    # s.quickSort()
    
    # s.selection()
    # s.insertion()
    # s.quick()
    s.testmergsort()

# testSort()


def testing():
    gp = undirectedGraph()

    # Insert edges based on your graph image
    gp.addEdge('a', 'b',10)
    gp.addEdge('a', 'c',15)

    gp.addEdge('a', 'd',20)
    gp.addEdge('d', 'e',11)

    # Run BFS from 0 to 9
    gp.dfs('a', 'e')
    gp.bfs('a','e')
    
# testing()


def testing_():
    tree = Testing([12,4,10,18,22,31,6,5])
    # data = [12,4,10,18,22,31,6,5]
    # for i in data:
    #     tree.insert(i)
    # print(tree.isMember(10))
    # print(tree.search(6))
    # tree.inorder()
    # tree.delete(10)
    # tree.inorder()
    # tree.bubleSort()
    # tree.selectionSort()
    # tree.insertionsort()
    # tree.quickSort()
    tree.mergeSort()

# testBinaryTree()
    
testing_()

