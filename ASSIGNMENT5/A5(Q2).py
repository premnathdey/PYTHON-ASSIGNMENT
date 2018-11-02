mylist=[]
i =int(input())
for j in range (i):
    d={'name':'name','age':'age','city':'city','height':'height'}
    d['name']=raw_input("Name:")
    d['age']=raw_input("Age:")
    d['city']=raw_input("City:")
    d['height']=raw_input("Height:")
    mylist.append(d)
print mylist
