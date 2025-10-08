from one import sortingLogic,stackTesting,queueTesting,linkedListTesting,treeTesting

def test():
    s = sortingLogic([12,32,1,21,65,87,3,12,23,21])
    #sorting

    # s.Buble()
    # s.selection()
    # s.insertion()
    # s.quick()
    # s.mergsort()

    #stack
    stack = stackTesting(5)
    # stack.push(10)
    # stack.push(20)
    # stack.push(30)
    # stack.push(40)
    # stack.push(50)
    # stack.pop()
    # stack.pop()
    # stack.pop()

    #queue
    queue = queueTesting()
    # queue.insert(10)
    # queue.insert(20)
    # queue.insert(30)
    # queue.insert(40)
    # queue.insert(50)
    # queue.dequeue()
    # queue.dequeue()
    # queue.dequeue()
    # queue.dequeue()
    # queue.dequeue()
    # queue.dequeue()
    # queue.dequeue()
    # queue.insert(10)
    # queue.insert(20)
    # queue.insert(30)
    # queue.insert(40)
    # queue.insert(50)
    # queue.insert(50)
    # queue.insert(50)

#linkedlist
def testLinkelist():
    ll = linkedListTesting()
#     ll.insertHead(10)
#     ll.insertHead(20)
#     ll.insertHead(30)
#     ll.insertHead(40)
#     ll.trav()
#     ll.deleEle(40)
#     print('after')
#     ll.trav()


# testLinkelist()


def testTree():
    tree=treeTesting()
    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(5)
    tree.insert(40)
    tree.insert(80)
    tree.insert(10)
    # print("preorder")
    # tree.preorder()
    # print("inorder")
    # tree.inorder()
    # print("postorder")
    # tree.postorder()
    tree.delete(30)
    tree.inorder()

testTree()