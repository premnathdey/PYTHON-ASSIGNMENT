print("Enter the array size you want to enter")
N=int(raw_input())
print("Enter the elements in the array")
A=list()
for i in range (N):
            x=int(raw_input())
            A.append(x)
print("Print the reverse order of Array")
for i in reversed(A):
            print(i)
