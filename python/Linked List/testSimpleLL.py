from SimpleLL import LinkeList
def testSimpleLL():

    #question 1
    ll  = LinkeList()


    assert ll.isEmpty() == True
    assert ll.getNoOfEle() == 0
    ll.addAtTail(10)
    ll.addAtTail(20)
    ll.addAtTail(30)
    ll.addAtTail(40)
    assert ll.getNoOfEle() == 4
    assert ll.search(40)==3
    ll.addAtHead(50)
    ll.addAtHead(60)
    ll.addAtHead(70)
    ll.addAtHead(80)
    assert ll.getNoOfEle() == 8
    assert ll.search(40)==7
    assert ll.deleteAtHead() == 80
    assert ll.getNoOfEle() == 7
    assert ll.deleteAtTail() == 40
    assert ll.getNoOfEle() == 6
    ll.addAfterEle(10,100)
    assert ll.getNoOfEle() == 7
    ll.DeleteAfterEle(20)
    assert ll.getNoOfEle() == 6
    ll.addAfterEle(20,1)
    ll.getLL()
    assert ll.getNoOfEle() == 7

    #question 2
    ll1  = LinkeList()
    ll2  = LinkeList()

    ll1.addAtTail(1)
    ll1.addAtTail(2)
    ll1.addAtTail(3)

    ll2.addAtTail(1)
    ll2.addAtTail(3)
    ll2.addAtTail(2)

    ll1.genCommenLinkedList(ll1.getHead(),ll2.getHead())


    #question 3
    ll = LinkeList()
    ll.addAtTail(1)
    ll.addAtTail(2)
    ll.addAtTail(3)
    ll.addAtTail(4)
    ll.addAtTail(5)
    assert ll.sumoOfLastN(2) == 9 


    #question 4 
    ll = LinkeList()
    ll.addAtTail(10)
    ll.addAtTail(20)
    ll.addAtTail(30)
    ll.addAtTail(40)
    ll.addAtTail(50)
    ll.reverseLL()

    #question 5
    ll = LinkeList()
    ll.addAtTail(1)
    ll.addAtTail(2)
    ll.addAtTail(3)
    ll.addAtTail(4)
    ll.addAtTail(5)
    ll.splitLL()
    
    # question 6 
    ll = LinkeList()
    ll.addAtTail(1)
    ll.addAtTail(2)
    ll.addAtTail(3)
    ll.addAtTail(4)
    ll.addAtTail(5)
    ll.addAtTail(5)
    ll.addAtTail(5)
    ll.addAtTail(4)
    ll.addAtTail(3)
    ll.addAtTail(2)
    ll.addAtTail(1)

    assert ll.isPalindrome() == True
    ll2 = LinkeList()
    ll2.addAtTail(11)
    ll2.addAtTail(2)
    ll2.addAtTail(3)
    ll2.addAtTail(4)
    ll2.addAtTail(5)
    ll2.addAtTail(5)
    ll2.addAtTail(5)
    ll2.addAtTail(4)
    ll2.addAtTail(3)
    ll2.addAtTail(2)
    ll2.addAtTail(1)
    assert ll2.isPalindrome() == False


    #question7 remove dublicates 
    ll2 = LinkeList()
    ll2.addAtTail(11)
    ll2.addAtTail(2)
    ll2.addAtTail(2)
    ll2.addAtTail(3)
    ll2.addAtTail(4)
    ll2.addAtTail(5)
    ll2.addAtTail(5)
    ll2.removeDublicates()
    ll2.getLL()

    # question 8 find mid
    ll = LinkeList()
    ll.addAtTail(1)
    ll.addAtTail(2)
    ll.addAtTail(3)
    ll.addAtTail(4)
    ll.addAtTail(5)
    ll.getLL()
    assert ll.getMid() == 3


    # question 9 
    ll = LinkeList()
    ll.addAtTail(1)
    ll.addAtTail(2)
    ll.addAtTail(3)
    ll.addAtTail(4)
    ll.addAtTail(5)

    ll.tail.next = ll.head  

    print("Before removing odd elements:")
    ll.displayCircular()

    # question 10 
    ll.removeOddFromCircular()


    print("After removing odd elements:")
    
    ll.displayCircular()

testSimpleLL()