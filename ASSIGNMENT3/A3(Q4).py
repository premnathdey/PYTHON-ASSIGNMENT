print("Enter the Size of your Array:")
N=int(input())
print("Enter the elements you want in the array")
A=list()
for i in range (N):
        n=int(raw_input())
        A.append(n)
from array import *
array_num = array('i', A)
print("Original array: "+str(array_num))
print("Length in bytes of one array item: "+str(array_num.itemsize))
