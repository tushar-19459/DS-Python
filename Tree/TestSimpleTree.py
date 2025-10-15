from  SimpleTree import SimpleTree

def testtree():
    tree = SimpleTree()
    assert tree.isEmpty()==True

    tree.insert(50)
    tree.insert(15)
    tree.insert(30)
    tree.insert(75)
    tree.insert(60)
    tree.insert(90)
    tree.insert(85)
    tree.insert(25)
    # tree.travers()
    # assert tree.isMember(60) == True
    # assert tree.isMember(100) == False
    tree.deleteNode(75)
    tree.travers()

testtree()