def findMinDiff(A, n):
    diff = 10**20
    for i in range(n-1):
        for j in range(i+1,n):
            if abs(A[i]-A[j]) < diff:
                    diff = abs(A[i] - A[j])
                    m=A[i]
                    k=i
                    M=A[j]
                    l=j
    print("The elements are",m,M)
    print("The positions are index",i,j)
    print(diff)
 
# Driver code
N=int(raw_input())
A=list()
for i in range (N):
         x=int(raw_input())
         A.append(x)
n = len(A)
findMinDiff(A, n)
 

