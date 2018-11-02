print("Enter the array size you want to enter")
N=int(raw_input())
print("Enter the elements in the array")
A=list()
for i in range (N):
            x=int(raw_input())
            A.append(x)
from array import *
array_num=array('i',A)
print("Original array: "+str(array_num))
print("Current memory address and the length in elements of the buffer: "+str(array_num.buffer_info()))
print("The size of the memory buffer in bytes: "+str(array_num.buffer_info()[1] * array_num.itemsize))
