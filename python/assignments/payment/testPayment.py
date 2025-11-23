from Payment import Manipal_Payment
class testPay:
    mp = Manipal_Payment()
    user1__mpsid = mp.register('tushar','2314432','1253231')
    user2__mpsid = mp.register('raj','2314432','1253231')
    user3__mpsid = mp.register('kishor','2314432','1253231')
    user4__mpsid = mp.register('anuj','2314432','1253231')
    user5__mpsid = mp.register('mahit','2314432','1253231')

    mp.credit(user1__mpsid,50000)
    mp.credit(user1__mpsid,7000)
    mp.debit(user1__mpsid,4000)
    mp.debit(user1__mpsid,4000)
    mp.debit(user1__mpsid,4000)
    mp.debit(user1__mpsid,4000)
    mp.debit(user1__mpsid,4000)
    mp.debit(user1__mpsid,4000)
    mp.debit(user1__mpsid,4000)
    mp.debit(user1__mpsid,4000)
    mp.debit(user1__mpsid,4000)

    mp.getTransaction(user1__mpsid)

    print('user count ',mp.admin_getcount())
    print("user details ",mp.admin_getdetail(user1__mpsid))

testPay()