print("Enter the array size you want to enter")
N=int(raw_input())
print("Enter the elements in the array")
A=list()
for i in range (N):
            x=int(raw_input())
            A.append(x)
from array import *
array_num = array('i',A)
p=int(raw_input())
print("Remove the pth item form the array:")
array_num.pop(p)
print("New array: "+str(array_num))

