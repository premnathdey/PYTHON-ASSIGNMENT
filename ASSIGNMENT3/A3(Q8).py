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
print("Remove the first occurrence of 3 from the said array:")
array_num.remove(3)
print("New array: "+str(array_num))
