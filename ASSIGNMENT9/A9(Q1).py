import threading
def multipleof31():
    for i in range(1,31):
        if i%3==0:
            print i
def multipleof32():
    for j in range (31,81):
        if j%3==0:
            print j
def multipleof33():
    for k in range (81,100):
        if k%3==0:
            print k

t1=threading.Thread(target=multipleof31)
t2=threading.Thread(target=multipleof32)
t3=threading.Thread(target=multipleof33)

t=[]
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

t.append(t1)
t.append(t2)
t.append(t3)

for m in t:
    m.join()
print 'Done'
