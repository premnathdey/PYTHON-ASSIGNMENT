import threading
def printhi():
    for i in range(10):
        print 'HI'
def printhello():
    for j in range (20):
        print 'HELLO'
def printbye():
    for k in range (50):
        print 'BYE'
t1=threading.Thread(target=printhi)
t2=threading.Thread(target=printhello)
t3=threading.Thread(target=printbye)

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

print 'MAIN THREAD EXITING'
