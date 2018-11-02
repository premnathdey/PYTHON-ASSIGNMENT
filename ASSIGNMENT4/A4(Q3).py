print "Enter the row and column"
N, M=map(int,raw_input().split())
A=[]
for i in range (N):
    A.append([])
    for j in range(M):
        s=int(input())
        A[i].append(s)
print "Demand"
D=[]
for i in range (N):
    k=int(input())
    D.append(k)
print "Supply"
S=[]
for i in range (M):
    k=int(input())
    S.append(k)
T=0
for i in range (N):
    for j in range (M):
        t=min(S[i],D[j])
        T=T+A[i][j]*t
        S[i]=S[i]-t
        D[j]=D[j]-t
print T
